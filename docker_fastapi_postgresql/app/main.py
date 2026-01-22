from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy_practise.orm import Session
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency do pobierania sesji z bazy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses/", response_model=schemas.ExpenseOut)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses", response_model=List[schemas.ExpenseOut])
def get_all_expenses(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()
    return expenses
