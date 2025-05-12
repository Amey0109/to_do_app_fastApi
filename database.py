from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base= declarative_base()

SQLALCHEMY_DATABASE_URL= "mssql+pyodbc://sa:4PLgm~(DpL.Gz-%@sqldev01.menetwork.com/amey?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal= sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally: 
        db.close()