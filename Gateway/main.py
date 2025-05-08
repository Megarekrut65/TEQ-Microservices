from decouple import config
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import httpx
from starlette.middleware.cors import CORSMiddleware

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


python_run_url = config("PYTHON_RUN")
python_test_url = config("PYTHON_TEST")

cpp_run_url = config("CPP_RUN")
cpp_test_url = config("CPP_TEST")

java_run_url = config("JAVA_RUN")
java_test_url = config("JAVA_TEST")

pl_url = config("PL_SIMILARITY")
nl_url = config("NL_SIMILARITY")

async def forward_request(service_url: str, request: Request):
    data = await request.body()
    headers = dict(request.headers)
    async with httpx.AsyncClient() as client:
        response = await client.post(service_url, content=data, headers=headers)
        return JSONResponse(content=response.json(), status_code=response.status_code)

# Example: 5 requests per second per IP
@app.post("/python/run/")
@limiter.limit("5/second")
async def gateway_python_run(request: Request):
    return await forward_request(python_run_url, request)

@app.post("/python/test/")
@limiter.limit("5/second")
async def gateway_python_test(request: Request):
    return await forward_request(python_test_url, request)

@app.post("/cpp/run/")
@limiter.limit("5/second")
async def gateway_cpp_run(request: Request):
    return await forward_request(cpp_run_url, request)

@app.post("/cpp/test/")
@limiter.limit("5/second")
async def gateway_cpp_test(request: Request):
    return await forward_request(cpp_test_url, request)

@app.post("/java/run/")
@limiter.limit("5/second")
async def gateway_java_run(request: Request):
    return await forward_request(java_run_url, request)

@app.post("/java/test/")
@limiter.limit("5/second")
async def gateway_java_test(request: Request):
    return await forward_request(java_test_url, request)

@app.post("/pl/similarity/")
@limiter.limit("5/second")
async def gateway_java_test(request: Request):
    return await forward_request(pl_url, request)

@app.post("/nl/similarity/")
@limiter.limit("5/second")
async def gateway_java_test(request: Request):
    return await forward_request(nl_url, request)