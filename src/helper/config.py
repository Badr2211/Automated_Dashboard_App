from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GOOGLE_API_KEY : str
    FILE_ALLOWED_TYPES :list
    class confg:
        env_file ='.env'


def get_settings():
    return Settings()