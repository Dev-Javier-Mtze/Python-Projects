import random

from poetry_demo.adapters.adapter_http import RetrieveResponseHttp
from poetry_demo.adapters.adapter_sql import RetrieveResponseSql
from poetry_demo.adapters.http_notificator import Notification
from poetry_demo.config import Settings

settings = Settings()

azar = random.randint(1, 2)
repo: RetrieveResponseHttp | RetrieveResponseSql
if azar == 1:
    Notification(":memory:").get_order()
    repo = RetrieveResponseSql(":memory:")
    user = repo.insert()
else:
    Notification(settings.http_url).get_order()
    repo = RetrieveResponseHttp(settings.http_url)


user = repo.get_order()
print(user)
