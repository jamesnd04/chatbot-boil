"use server"

# external
from fastapi import FastAPI
from openai import OpenAI

# internal
from src.model import Message, Role
from src.io import ChatInput
from dotenv import load_dotenv
import os

app = FastAPI()


# make the client using the api key from the .env file
load_dotenv()
api_key = os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/chat")
def chat(input: ChatInput) -> Message:
    try:
        content = " ".join([str(message.content) for message in input.messages])
        completion = client.chat.completions.create(
            model="gpt-4o-mini", messages=[{"role": "user", "content": content}]
        )
        return Message(
            role=Role.ASSISTANT, content=completion.choices[0].message.content
        )
    except Exception as e:
        return e
