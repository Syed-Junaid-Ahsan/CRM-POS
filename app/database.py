from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#DATABASE_URL = "mysql+pymysql://root:Junaid.03@localhost/shop_management"
# pymysql://root:Junaid.03@localhost/shop_management
DATABASE_URL = "mysql+pymysql://root:Junaid.03@monorail.proxy.rlwy.net:40121/shop_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


