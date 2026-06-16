from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "สวัสดี เต๋า! API พร้อมแล้ว"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"สวัสดี {name}!"}