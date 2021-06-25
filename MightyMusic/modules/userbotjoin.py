# Copyright (C) 2021 Vc-MusicINDO Yunus-ZEND 
#
# Free Software Foundation, LICENSE GNU GPL v3.0 <https://github.com/Yunus-ZEND/MightyProject/blob/MightyProject/LICENSE>
# Everyone is permitted to copy and distribute verbatim copies
# of this license userbotjoin, but changing it is not allowed.
#
# Creator And Contributor

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from MightyMusic.helpers.decorators import authorized_users_only, errors
from MightyMusic.services.callsmusic.callsmusic import client as USER
from MightyMusic.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asisten sudah ada di obrolan Anda</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n Pengguna {user.first_name} tidak bisa join ke group kamu, mungkin krn sudah di ban atau ada kesalahan."
            "\n\natau tidak tambahkan secara manual asisten ke dalam group kamu</b>",
        )
        return
    await message.reply_text(
        "<b>asisten berhasil masuk ke group kamu</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Pengguna tidak dapat meninggalkan grup Anda! Mungkin menunggu floodwait."
            "\n\nAtau tidak kick asisten secara manual</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        await message.reply("Asisten keluar dari semua grup")
        for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Jadikan saya admin dulu di Channel kamu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "MightyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>asisten berhasil masuk ke Channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} asisten tidak bisa join Channel kamu, mungkin terkena efek ban atau ada kesalahan."
            "\n\nAtau tidak tambahkan asisten secara manual</b>",
        )
        return
    await message.reply_text(
        "<b>asisten berhasil masuk ke Channel kamu</b>",
    )
