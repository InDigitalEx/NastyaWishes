from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    bot_token: SecretStr
    database_url: SecretStr
    debug: bool

    model_config = SettingsConfigDict(
        env_file=('config', '.config'),
        env_file_encoding='utf-8'
    )


config = Config()
