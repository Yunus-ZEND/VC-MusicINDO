# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from MightyMusic.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("Memulai Gcast")
        if not message.reply_to_message:
            await lol.edit("Balas pesan teks apa pun ke gcast tuan")
            return
        msg = message.reply_to_message.text
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"Sedang.. Mengirim pesan : {sent} chats. Gagal : {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Sedang.. Mengirim pesan : {sent} chats. Gagal : {failed} chats.")
            await asyncio.sleep(0.7)
        await message.reply_text(f"Berhasil Mengirim Pesan Ke {sent} chats. Gagal {failed} chats.")
