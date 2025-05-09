import httpx
from decouple import config
from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.cors import CORSMiddleware

from router_map import ROUTE_MAP

app = FastAPI()

origins = [
    config("ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."}
    )


def match_route(path: str) -> str | None:
    for prefix in ROUTE_MAP:
        if prefix.endswith(path):
            return ROUTE_MAP[prefix]
    return None


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
@limiter.limit("5/second")
async def proxy(path: str, request: Request):
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        url = match_route(path)
        if url is None:
            return JSONResponse(status_code=404,
                                   content={"detail": "Endpoint not found"})

        response = await client.request(
            request.method,
            url,
            headers={key: value for key, value in request.headers.items() if key != "host"},
            content=await request.body()
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
