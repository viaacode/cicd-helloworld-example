from litestar import Litestar, get
from viaa.configuration import ConfigParser


def create_app():
    config = ConfigParser().app_cfg

    name = config["name"]
    secret = config["secret"]

    @get("/")
    async def hello_world() -> dict[str, str]:
        return {name: secret}

    return Litestar(route_handlers=[hello_world])
