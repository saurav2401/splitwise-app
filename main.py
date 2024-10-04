from fastapi import FastAPI


app = FastAPI()

expenses: Dict[int,Expense] = {}
expense_id_counter = 1


@app.post ("/expense/",response_model= Expense)
def create_expense(expense:ExpenseCreate):
  global expense_id_counter
  for user_id in expense.users:
    if user_id not in expense.users:
      raise HTTPException(status_code=400,detail="User not found")
    
    split_amount = round (expense.amount / len(expense.users),2)
    split_details = {user_id:split_amount for user_id in expense.users}
  # new_expense = Expense(id = expense_id_counter, **expense.dict())
  # expenses[expense_id_counter] = new_expense
  # expense_id_counter += 1
  # return new_expense

@app.get("/expenses/{expense_id}", response_model= Expense)
def get_expense(expense_id: int):
  expense = expenses.get(expense_id)
  if not expense:
    raise HTTPException(status_code=404, detail="Expense not found")
  return expense