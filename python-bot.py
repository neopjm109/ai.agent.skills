import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ChatAction
from openai import AsyncOpenAI

load_dotenv()
TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")

client = AsyncOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

async def ask_llm(prompt: str):
    response = await client.chat.completions.create(
        model="gemma-4-e4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

async def typing(chat_id, bot):
    while True:
        await bot.send_chat_action(
            chat_id=chat_id,
            action=ChatAction.TYPING
        )
        await asyncio.sleep(4)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    task = asyncio.create_task(
        typing(update.effective_chat.id, context.bot)
    )
    try:
        answer = await ask_llm(update.message.text)
    finally:
        task.cancel()
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# command 응답
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()
