import pytest

from poetry_demo.int_module_6_cache import Adapter, Middle, Port


@pytest.fixture
def adapter_sql():
    service = Middle()
    return Adapter(service)


def test_get_order_sql(adapter_sql):
    assert hasattr(adapter_sql, "get_data")