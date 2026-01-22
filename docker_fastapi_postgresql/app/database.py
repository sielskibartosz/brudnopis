import time
from sqlalchemy_practise import create_engine
from sqlalchemy_practise.exc import OperationalError
from sqlalchemy_practise.ext.declarative import declarative_base
from sqlalchemy_practise.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Próbujemy połączyć się z bazą do 10 razy z 2-sekundową przerwą
for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        # testowe połączenie
        connection = engine.connect()
        connection.close()
        print("✅ Połączono z bazą danych!")
        break
    except OperationalError:
        print(f"⏳ Próba {attempt + 1}/10: baza danych jeszcze nie gotowa, czekam 2 sekundy...")
        time.sleep(2)
else:
    raise Exception("❌ Nie udało się połączyć z bazą danych po 10 próbach.")

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
