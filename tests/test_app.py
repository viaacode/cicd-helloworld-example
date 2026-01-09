from litestar.testing import TestClient

from app.app import app


def test_hello_world() -> None:
    with TestClient(app=app) as client:
        assert client.get("/").json() == {"hello": "world"}
