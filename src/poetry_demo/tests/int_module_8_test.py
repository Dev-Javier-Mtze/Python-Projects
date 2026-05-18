import pytest

from poetry_demo.adapters.adapter_http import RetrieveResponseHttp
from poetry_demo.adapters.adapter_sql import RetrieveResponseSql
from poetry_demo.config import Settings
from poetry_demo.domain.ports import CreateOrder

settings = Settings()


@pytest.fixture
def adapter_sql():
    return RetrieveResponseHttp(settings.http_url)


def test_port_sql(adapter_sql):
    assert isinstance(adapter_sql, CreateOrder)


def test_get_order_sql(adapter_sql):
    assert hasattr(adapter_sql, "get_order")


@pytest.fixture
def adapter_http():
    return RetrieveResponseSql(":memory:")


def test_port_http(adapter_http):
    assert isinstance(adapter_http, CreateOrder)


def test_get_order_http(adapter_http):
    assert hasattr(adapter_http, "get_order")
