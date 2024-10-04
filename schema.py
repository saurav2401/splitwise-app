from pydantic import BaseModel
from typing import List

class ExpenseCreate(BaseModel):
  description: str
  amount: float
  users: List[int]