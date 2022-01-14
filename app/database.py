from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# while True:
#     try:
#         conn = psycopg2.connect(host= "localhost" , database = "fast_api", user = "fayaz" , password = "password123", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection successfull")
#         break
#     except Exception as error:
#         print  ("error" , error)
#         time.sleep(2)
