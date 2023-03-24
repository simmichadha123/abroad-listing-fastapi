import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

def getEnv(key:str):
    return os.getenv(key)

class Setting(BaseSettings):
    VERSION = "0.0.1"
    DESCRIPTION = "FAST API for college project"
    MYSQL_USER: str = os.getenv("MASTER_DB_USER", "")
    MYSQL_PASSWORD: str = os.getenv("MASTER_DB_PASSWORD", "")
    MYSQL_SERVER: str = os.getenv("SLAVE_DB_HOST", "localhost")
    MYSQL_PORT: str = os.getenv("SLAVE_DB_PORT", 3306)  # default mysql port is 5432
    MYSQL_DB: str = os.getenv("MASTER_DB_NAME", "")
    db_url: str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    class Config:
        env_file = ".env"


setting  = Setting()