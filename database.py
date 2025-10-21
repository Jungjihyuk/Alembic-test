import os
from pathlib import Path 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

ENV_PATH = Path(__file__).parent / '.env'

load_dotenv(ENV_PATH)

DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "database_name")

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,  # 확정을 자동으로 주지 않겠다 
                            autoflush=False,   # 새로고침을 자동으로 하지 않겠다 
                            bind=engine)       # 어떤 데이터베이스랑 연결시켜서 세션을 만들건지 지정

Base = declarative_base()

def create_tables():
    """ORM 모델(파이썬 클래스)를 
    데이터 베이스 테이블로 생성하는 함수"""
    
    # engine과 연결된 데이터베이스에 데이터 베이스 테이블 생성
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try: 
        yield db    # yield가 포함되어 있는 함수는 generator 
    finally: 
        db.close()
        