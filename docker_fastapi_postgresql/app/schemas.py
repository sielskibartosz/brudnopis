from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    first_name: str
    last_name: str
    amount: float

class ExpenseOut(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True
