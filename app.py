
from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide

app = FastAPI(title="Python CI/CD Calculator API")


@app.get("/")
def home():
    return {
        "message": "Calculator API is running successfully with CI/CD!",
        "docs": "/docs"
    }


@app.get("/add")
def addition(a: float, b: float):
    return {"result": add(a, b)}


@app.get("/subtract")
def subtraction(a: float, b: float):
    return {"result": subtract(a, b)}


@app.get("/multiply")
def multiplication(a: float, b: float):
    return {"result": multiply(a, b)}


@app.get("/divide")
def division(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
