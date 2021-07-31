from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CQ2C8OgACJONhBArvX6vNWpIbK9InBJf8WHUEsAACBgMAAobvIFRqH2iAi7BOMiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Sadew](https://t.me/Darkridersslk).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Sadew451/GroupMusicPlayerBot")
                  ],[
                    InlineKeyboardButton(
                        "𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝘽𝙊𝙏𝙨 Support", url="https://t.me/Theekshana_Support"
                    ),
                    InlineKeyboardButton(
                        "𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇x", url="https://t.me/Theekshana_Official"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/ImGroupMusicBot?startgroup=true"
                        
                     ),
                    InlineKeyboardButton(
                         "BOTs Developer", url="https://t.me/Pawan_Theekshana"
                    )   
                ]    
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇", url="https://t.me/https://t.me/Theekshana_Official")
                ]
            ]
        )
   )


