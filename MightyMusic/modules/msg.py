import os
from MightyMusic.config import SOURCE_CODE,ASSISTANT_NAME,UPDATES_CHANNEL,PROJECT_NAME,SUPPORT_GROUP,OWNER_NAME
class Messages():
      START_MSG = "**Hallo [{}](tg://user?id={})!**\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n📮 Saya adalah bot canggih yang dibuat untuk memutar musik di obrolan suara Grup & Saluran Channel Telegram.\n\n📝 Ketik /help untuk mendapat info dari saya.\n╭═════════════\n├◈ Asisten: @{ASSISTANT_NAME}\n├◈ Owner: @{OWNER_NAME}\n╰╼════════════"
      HELP_MSG = [
        ".",
f"""
**Hy lagi kamu bertemu lagi dengan saya {PROJECT_NAME}

⚪️ {PROJECT_NAME} bisa memutar musik baik itu di VC Group atau VC Channel

⚪️ Nama Asisten >> @{ASSISTANT_NAME}\n\nKlik tombol dibawah untuk melihat intruksi lain**
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Beberapa Command**

**=>> Memainkan Lagu 🎧**

• /play <nama lagu> : putar lagu yang Anda minta
• /play <url youtube> : Putar lagu melalui balasan url youtube
• /play <balas ke audio> : putar file balasan
• /dplay <nama lagu> : putar lagu yang Anda minta melalui deezer
• /splay <nama lagu> : putar lagu yang Anda minta melalui jio saavn

**=>> Playback ⏯**

- /player: buka panel pengaturan pemutar musik
- /skip: putar lagu berikutnya
- /pause: jeda pemutaran lagu
- /resume: melanjutkan pemutaran lagu
- /end: hentikan pemutaran musik
- /current: Tampilkan sedang diputar
- /playlist: Tampilkan daftar yang sedang diputar

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Putar Musik Di Channel 📮**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
