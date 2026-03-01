from pydantic import BaseModel, Field, field_validator
import re

class User(BaseModel):
    name: str
    id: int

class UserWithAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    def check_bad_words(cls, value):
        bad_words = ["кринж", "рофл", "вайб"]

        for word in bad_words:
            if re.search(word, value, re.IGNORECASE):
                raise ValueError("Использование недопустимых слов")

        return value