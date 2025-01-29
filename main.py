import os
import chainlit as cl
import ollama
from dotenv import load_dotenv

load_dotenv()


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])


@cl.on_message
async def on_message(message: cl.Message):
    chat_history = cl.user_session.get("chat_history")
    chat_history.append({"role": "user", "content": message.content})

    resp = cl.Message(content="")
    chat_resp = ollama.chat(
        model=os.getenv("R1_VARIANT", "deepseek-r1:7b"),
        messages=chat_history,
        stream=True,
    )

    final = ""
    for cr in chat_resp:
        t = cr["message"]["content"]
        final += t
        await resp.stream_token(t)

    chat_history.append(
        {
            "role": "assistant",
            "content": final,
        }
    )

    cl.user_session.set("chat_history", chat_history)
    await resp.send()
