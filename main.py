from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dupa import SpendingDB  # zakładam, że masz klasę w spending_db.py

app = FastAPI()
db = SpendingDB("identifier.sqlite")  # podaj ścieżkę do swojej bazy

# Modele danych
class User(BaseModel):
    id: int
    name: str
    surname: str

class Spending(BaseModel):
    title: str
    price: float
    user_id: int

# Endpoint: dodawanie użytkownika
@app.post("/users/")
def add_user(user: User):
    try:
        db.add_user(user.id, user.name, user.surname)
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błąd: {e}")

# Endpoint: dodawanie wydatku
@app.post("/spendings/")
def add_spending(spending: Spending):
    try:
        db.add_spending(spending.title, spending.price, spending.user_id)
        return {"message": "Spending added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błąd: {e}")

# Endpoint: pobieranie listy użytkowników
@app.get("/users/")
def get_users():
    try:
        return db.list_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd: {e}")

# Endpoint: pobieranie listy wydatków
@app.get("/spendings/")
def get_spendings():
    try:
        return db.list_spendings()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd: {e}")
