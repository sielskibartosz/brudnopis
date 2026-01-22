from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))

# Tworzymy silnik bazy SQLite - plik users.db w aktualnym folderze
engine = create_engine('sqlite:///users.db', echo=True)

# Tworzymy wszystkie tabele (tu: tylko users)
Base.metadata.create_all(engine)

print("Baza i tabela 'users' zostały utworzone.")
