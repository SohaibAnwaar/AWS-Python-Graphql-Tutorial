from typing import Optional
from pydantic import BaseSettings

# This is a pydantic model for the enviroment variables


class Settings(BaseSettings):
    appsync_endpoint: str
    api_key_appsync: str
    aws_elastic_cache_host: str
    aws_elastic_cache_port: int
    access_key: str
    access_secret: str


    class Config:
        env_file = ".env"


settings = Settings()
