import asyncio
import random
from AbdoX import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://telegra.ph/file/93c01d015d6c369948d03.jpg"


MESSAGE = f"""- بوت تشغيل القران  الكريم  بالقنوات والجروبات 

وبدون تهنيج او تقطيع او توقف وكمان البوت في مميزات جامدة⚡️♥️.

ارفع البوت ادمن ف قناتك او جروبك واستمتع بجوده صوت و سرعه خياليه ⚡️♥️

معرف البوت 🎸 [ @{app.username} ]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""


BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("خدني لجروبك 🥺♥",url=f"https://t.me/{app.username}?startgroup=True")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo.file_id, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())



MazenMusic_responses = [
    f"""- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه\n\nوبدون تهنيج او تقطيع او توقف وكمان البوت فيه مميزات جامدة ⚡️♥️.\n\nارفع البوت ادمن ف قناتك او جروبك واستمتع بجوده صوت و سرعه خياليه ⚡️♥️\n\n
 معرف البوت 🎸 [@{app.username}]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""
       
]

@app.on_message(filters.command(["ترويج عام"], ""), group=39)
async def MazenMusic_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(MazenMusic_responses)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك 🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply(
        f"{bar}",
        reply_markup=keyboard
    )
