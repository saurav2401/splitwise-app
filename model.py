from pydantic import BaseModel
from typing import List

class Expense(BaseModel):
  id: int
  description: str
  amount: float
  users: List[int]

class User(BaseModel):
  id: int
  name: str