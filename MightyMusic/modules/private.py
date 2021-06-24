# Creator by Stereo Music Project

import logging
from StereoMusic.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StereoMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,SUPPORT_CHANNEL,BOT_USERNAME,OWNER_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 Tambahkan saya ke group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url=f"https://t.me/{SUPPORT_CHANNELdownload.                  InlineKeyboardButton(
                        "📍 Group", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton(
                        "📩 Instagram", url=f"https://insragram.com/ariasinathrya?utm_medium=copy_link")
                ]   InlineKeyboardButton(
            ]           "☕ Founder", url=f"https://t.me/SilenceSpe4ks")
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} telah diaktifkan**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☕ Owner Bot", url=f"https://t.me/{OWNER_USERNAME}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Tambahkan saya ke group ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '🔊 Channel Updates', url=f"https://t.me/{SUPPORT_CHANNEL}"),
             InlineKeyboardButton(text = '🎛 Group Support', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = '🎙 Owner Bot', url=f"https://t.me/{OWNER_USERNAME}"),
             InlineKeyboardButton(text = '☕ Created by', url=f"https://t.me/SilenceSpe4ks")],
            [InlineKeyboardButton(text = '↩ Kembali', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'Kembali', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Next', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**<b>Hallo👋 {message.from_user.first_name} saya adalah {PROJECT_NAME}\n
Saya Adalah Bot Music Group, Yang Dapat Memutar Lagu Di Voice Chat Group Anda Dengan Mudah
Saya Memiliki Banyak Fitur Seperti :
•Memutar Musik.
•Mendownload Lagu.
•Mencari Lagu Yang Ingin Di putar Atau Di download.
•Gunakan Perintah >>/help<< Untuk Mengetahui Fitur Lengkapnya

🙏 Terimakasih Untuk : {OWNER}


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📲 Klik disini untuk bantuan", url=f"https://t.me/{BOT_USERNAME}?start"
                     ),
                     InlineKeyboardButton(
                          "☕ Created by", url=f"https://t.me/SilenceSpe4ks"
                     ),
                     InlineKeyboardButton(
                          "🎙 Group Support", url=f"https://t.me/luciddreaams"
                    )
                ]
            ]
        ),
    )
