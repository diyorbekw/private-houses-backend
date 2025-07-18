from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    access_token_expire_minutes: int = 30
    access_secret_key: str
    algorithm: str = "HS256"


    model_config = SettingsConfigDict(env_file=".env")
 
    
    @property
    def connection_string(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
 