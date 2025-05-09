import decouple

ROUTER_LIST = [
    "/python/run",
    "/python/test",
    "/cpp/run",
    "/cpp/test",
    "/java/run",
    "/java/test",
    "/pl/similarity",
    "/nl/similarity"
]

ROUTE_MAP = {}

for router in ROUTER_LIST:
    ROUTE_MAP[router+"/"] = decouple.config("ROUTE_"+router)