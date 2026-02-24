from fastapi import FastAPI

app = FastAPI(title="간단한 계산기 API")

@app.get("/")
def read_root():
    return {"message": "서버가 정상적으로 작동 중입니다."}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}

@app.get("/hello")
def say_hello():
    return {"message": "Hello SonarCloud!"}