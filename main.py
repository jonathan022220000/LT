from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculatorInput(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
async def calculate(data: CalculatorInput):
    if data.operation == "add":
        result = data.num1 + data.num2
    elif data.operation == "subtract":
        result = data.num1 - data.num2
    elif data.operation == "multiply":
        result = data.num1 * data.num2
    elif data.operation == "divide":
        if data.num2 == 0:
            return {"error": "Division by zero"}
        result = data.num1 / data.num2
    else:
        return {"error": "Invalid operation"}
    return {"result": result}