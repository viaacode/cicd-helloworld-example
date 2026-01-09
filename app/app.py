from litestar import Litestar, get
from viaa.configuration import ConfigParser
from viaa.observability import logging


def create_app():
    config_parser = ConfigParser()
    log = logging.get_logger(__name__, config=config_parser)

    app_cfg = config_parser.app_cfg
    name = app_cfg["name"]
    secret = app_cfg["secret"]

    @get("/")
    async def hello_world() -> dict[str, str]:
        log.info(f"{name}: {secret}")
        return {name: secret}

    return Litestar(route_handlers=[hello_world])
