from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="25901632",
    api_hash="caac15797ce3785ae427cda6318b85c9",
    bot_token="6402002890:AAGucQU_ajXkA1OGzZpqbKAuBcB_QRkNoUA",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "CRAZ_UP"
    await bot.send_message(AFROTOO, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
