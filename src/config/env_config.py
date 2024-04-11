from pydantic_settings import BaseSettings

class EnvironmentConfig(BaseSettings):
    env: str = 'development'
    port: int = 3000

    class Config:
        env_file = ".env"

config = EnvironmentConfig()