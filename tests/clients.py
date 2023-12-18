import os

import openapi_client
from dotenv import load_dotenv

from models.base import Base
from nguylinc_python_utils.sqlalchemy import SessionManager

load_dotenv()
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:34200",
)

api = openapi_client.ApiClient(configuration)
projectApi = openapi_client.ProjectApi(api)

session = SessionManager(Base)
path = os.path.join(os.getenv("HOME"), "workplace", "SakuinSeizouki", "SakuinSeizoukiApi", "api", "sqlite.db")
session.update(path)
