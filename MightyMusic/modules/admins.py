# Copyright (C) 2021 Vc-MusicINDO Yunus-ZEND 
#
# Free Software Foundation, LICENSE GNU GPL v3.0 <https://github.com/Yunus-ZEND/MightyProject/blob/MightyProject/LICENSE>
# Everyone is permitted to copy and distribute verbatim copies
# of this license admins, but changing it is not allowed.
#
# Creator And Contributor

from asyncio.queues import QueueEmpty
from MightyMusic.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from MightyMusic.function.admins import set
from MightyMusic.helpers.channelmusic import get_chat_id
from MightyMusic.helpers.decorators import authorized_users_only, errors
from MightyMusic.helpers.filters import command, other_filters
from MightyMusic.services.callsmusic import callsmusic


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Cache Admin berhasil di refresh!")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("❗ Tidak ada yang dimainkan!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("▶️ Dijeda!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("❗ Tidak ada yang bisa dijeda!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("⏸ Dilanjutkan!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada lagu yang diputar!")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("❌ Menghentikan pemutaran!")


@Client.on_message(command("skip") & other_filters)
@errors
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada yang diputar untuk di skip!")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"◎› Skip Lagu **{skip[0]}**\n◎› Sekarang dimainkan **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache di resfresh!")
