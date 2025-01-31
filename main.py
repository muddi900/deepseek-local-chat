import os
import chainlit as cl
import ollama
from tqdm import tqdm

import logging
import asyncio

import ollama
import chainlit as cl


if os.getenv("R1_VARIANT", "") not in ollama.ps().models:
    pull = ollama.pull(os.getenv("R1_VARIANT", "deepseek-r1:1.5b"), stream=True)

    for _ in tqdm(pull):
        pass


@cl.password_auth_callback
async def pass_auth(user: str, pwd: str):
    return cl.User(
        identifier="admin", metadata={"role": "admin", "provider": "credentrials"}
    )


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])


@cl.on_message
async def on_message(message: cl.Message):
    chat_history = cl.user_session.get("chat_history")
    chat_history.append({"role": "user", "content": message.content})
    resp = cl.Message(content="")

    chat_resp = ollama.chat(
        model=os.getenv("R1_VARIANT", ""),
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


if __name__ == "__main__":
    if os.getenv("CL_DEBUG"):
        from chainlit.cli import run_chainlit

        run_chainlit(__file__)
