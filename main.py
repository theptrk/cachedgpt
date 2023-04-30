import os
import openai

from dotenv import load_dotenv

from tortoise.exceptions import DoesNotExist
# Load the environment variables from the .env file

# pylint: disable=E0611,E0401
from typing import List

from fastapi import FastAPI
from models import ChatCompletionModel
from pydantic import BaseModel

from tortoise.contrib.fastapi import register_tortoise

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Tortoise ORM FastAPI example")

class ChatItem(BaseModel):
    role: str
    content: str

class ChatCompletionInput(BaseModel):
    messages: List[ChatItem]


async def openai_chat_request(messages, model="gpt-3.5-turbo"):
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        return completion
    except Exception as e:
        print("error in openai_chat_request: " + str(e))
        return None


@app.post("/chatCompletion")
async def chat_completion(chat_completion_input: ChatCompletionInput):
    messages = chat_completion_input.messages
    messages_dicts = [item.dict() for item in messages]
    try:
        existing_chat_completion = await ChatCompletionModel.get(messages={"messages": messages_dicts})
        return {"message": "Data already exists in the database", "data": existing_chat_completion}
    except DoesNotExist:
        response = await openai_chat_request(messages_dicts, model="gpt-3.5-turbo")
        chat_completion = ChatCompletionModel(
            messages={"messages": messages_dicts},
            response=response
        )
        await chat_completion.save()
        return {"message": "Data saved successfully", "data": chat_completion}


@app.get("/chatCompletions")
async def get_chat_completions():
    chat_completions = await ChatCompletionModel.all()
    return chat_completions


register_tortoise(
    app,
    db_url="sqlite://:memory:",
    # db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)