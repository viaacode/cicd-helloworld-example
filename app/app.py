from litestar import Litestar, get, status_codes
from viaa.configuration import ConfigParser
from viaa.observability import logging


def create_app() -> Litestar:
    config_parser = ConfigParser()
    log = logging.get_logger(__name__, config=config_parser)

    app_cfg = config_parser.app_cfg
    name = app_cfg["name"]
    secret = app_cfg["secret"]

    @get("/")
    async def hello_world() -> dict[str, str]:
        log.info(f"{name}: {secret}")
        return {name: secret}

    @get("/healthz", status_code=status_codes.HTTP_204_NO_CONTENT)
    async def health() -> None:
        return None

    @get("/readyz", status_code=status_codes.HTTP_204_NO_CONTENT)
    async def ready() -> None:
        return None

    return Litestar(route_handlers=[hello_world, health, ready])
