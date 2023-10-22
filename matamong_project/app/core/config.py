from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your secret key here. you should set this in .env file or different way for security"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    title: str = "FastAPI Starter"
    version: str = "0.1.0"
    PROJECT_NAME: str = "FastAPI Starter"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    

    """
    Test Settings
    """
    # TEST_DATABASE_URL: str
    # TEST_USER_EMAIL: str


    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
