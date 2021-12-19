# Copyright (C) 2021 Vc-MusicINDO Yunus-ZEND
#
# Free Software Foundation, LICENSE GNU GPL v3.0 <https://github.com/Yunus-ZEND/MightyProject/blob/MightyProject/LICENSE>
# Everyone is permitted to copy and distribute verbatim copies
# of this license channeladmin, but changing it is not allowed.
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


@Client.on_message(
    filters.command(["channelpause", "cpause"]) & filters.group & ~filters.edited
)
@errors
@authorized_users_only
async def pause(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except ConnectionError:
        await message.reply("Apakah obrolan Anda terhubung?")
        return
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("❗ Tidak ada yang bermain!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("▶️ Dijeda!")


@Client.on_message(
    filters.command(["channelresume", "cresume"]) & filters.group & ~filters.edited
)
@errors
@authorized_users_only
async def resume(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except Exception:
        await message.reply("Apakah obrolan Anda terhubung?")
        return
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("❗ Tidak ada yang dijeda!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("⏸ Dilanjutkan!")


@Client.on_message(
    filters.command(["channelend", "cend"]) & filters.group & ~filters.edited
)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except ConnectionError:
        await message.reply("Apakah obrolan Anda terhubung?")
        return
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada yang streaming!")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("❌  Streaming di stop!")


@Client.on_message(
    filters.command(["channelskip", "cskip"]) & filters.group & ~filters.edited
)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except ConnectionError:
        await message.reply("Apakah obrolan Anda terhubung?")
        return
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Tidak ada yang bermain untuk dilewati!")
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
    await message.reply_text(
        f"- Dilewati **{skip[0]}**\n- Sedang dimainkan **{qeue[0][0]}**"
    )


@Client.on_message(filters.command("channeladmincache"))
@errors
async def admincache(client, message: Message):
    try:
        conchat = await client.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except ConnectionError:
        await message.reply("Apakah obrolan Anda terhubung?")
        return
    set(
        chid,
        [
            member.user
            for member in await conchat.linked_chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Cache admin disegarkan!")
