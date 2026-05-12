import random

from poetry_demo.adapters.adapter_http import RetrieveResponseHttp
from poetry_demo.adapters.adapter_sql import RetrieveResponseSql
from poetry_demo.adapters.http_notificator import Notification

azar = random.randint(1, 2)
repo: RetrieveResponseHttp | RetrieveResponseSql
if azar == 1:
    Notification(":memory:").get_order()
    repo = RetrieveResponseSql(":memory:")
    user = repo.insert()
else:
    Notification("https://httpbin.org/get").get_order()
    repo = RetrieveResponseHttp("https://httpbin.org/get")


user = repo.get_order()
print(user)
