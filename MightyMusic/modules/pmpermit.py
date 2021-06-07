from pyrogram import Client
import asyncio
from MightyMusic.config import SUDO_USERS, PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from MightyMusic.services.callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Hy kamu, Ini adalah layanan asisten .\n\n ❗️ Rules:\n   ◎› Tidak ada obrolan yang diizinkan\n   ◎› Dilarang melakukan spam \n\n 📝 **KIRIM LINK UNDANGAN GROUP ATAU USERNAME JIKA USERBOT TIDAK BISA JOIN GROUP ANDA.**\n\n ⚠️ Penolakan: Jika Anda mengirim pesan di sini berarti admin akan melihat pesan Anda dan bergabung dengan obrolan\n    ◎›  Jangan tambahkan pengguna ini ke grup rahasia.\n   ◎› Jangan Bagikan info pribadi di sini\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit Diaktifkan")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit Dinonaktifkan")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk PM karena pesan keluar")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("ok", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Menyetujui PM dari orang ini")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("blok", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Menolak PM dari orang ini")
        return
    message.continue_propagation()    
