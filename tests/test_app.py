from litestar.testing import TestClient

from app.app import create_app


def test_hello_world(monkeypatch) -> None:
    monkeypatch.setenv("NAME", "hello")
    monkeypatch.setenv("SECRET", "world")

    app = create_app()
    with TestClient(app=app) as client:
        assert client.get("/").json() == {"hello": "world"}
