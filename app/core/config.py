from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """ """
    BOT_TOKEN:str
    WEATHER_HOST:str
    WEATHER_APPID:str

    class Config():
        case_sensitive = True
        env_file ='.env'

settings = Settings()