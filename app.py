from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, UserWithAge, Feedback

app = FastAPI()

@app.get("/json")
def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@app.get("/")
def get_html():
    return FileResponse("index.html")

@app.post("/calculate")
def calculate(numbers: dict):
    num1 = numbers.get("num1", 0)
    num2 = numbers.get("num2", 0)
    return {"result": num1 + num2}

user = User(
    name="Ваше Имя и Фамилия",
    id=1
)

@app.get("/users")
def get_user():
    return user

@app.post("/user")
def check_user(user: UserWithAge):
    is_adult = user.age >= 18

    return {
        "name": "Dudnik Valeriy",
        "age": user.age,
        "is_adult": is_adult
    }

feedbacks = []

@app.post("/feedback")
def send_feedback(feedback: Feedback):
    feedbacks.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }