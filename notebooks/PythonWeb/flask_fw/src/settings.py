import os


class Config:
    DEBUG = True
    TESTING = True
    DATABASE_TYPE = "sqlite"
    DATABASE_CONN = "localhost.db"
    CORS_HEADERS = "Content-Type"
    URL = "http://localhost:8000"
