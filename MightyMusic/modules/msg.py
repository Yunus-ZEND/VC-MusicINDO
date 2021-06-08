import os
from MightyMusic.config import SOURCE_CODE,ASSISTANT_NAME,UPDATES_CHANNEL,PROJECT_NAME,SUPPORT_GROUP,OWNER_USERNAME
class Messages():
      START_MSG = "**Hallo [{}](tg://user?id={})!**\n━━━━━━━━━━━━━━━━━━━━━━━━\n📮 Saya adalah bot canggih yang dibuat untuk memutar musik di obrolan suara Grup & Saluran Channel Telegram.\n\n📝 Ketik /help untuk mendapat info dari saya.\n━━━━━━━━━━━━━━━━━━━━━━━━\n🎻 Selamat menikmati sensasi mendengarkan musik di VC GROUP/ CHANNEL kamu."
      HELP_MSG = [
        ".",
f"""
**Hy lagi kamu bertemu lagi dengan saya {PROJECT_NAME}

⚪️ {PROJECT_NAME} bisa memutar musik baik itu di VC Group atau VC Channel

⚪️ Nama Asisten >> @{ASSISTANT_NAME}\n\nKlik tombol dibawah untuk melihat intruksi lain**
◎› Owner Bot >> @{OWNER_USERNAME}
◎› Owner Project >> @ZendYNS
""",

f"""
**Pengaturan Utama**

1) Membuat bot admin (Group dan di channel jika menggunakan cplay)
2) Mulai obrolan suara
3) Coba /play [nama lagu] pertama kali oleh admin
*) Jika userbot bergabung nikmati musik, Jika tidak tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi

**Untuk Channel Music Play**
1) Jadikan saya admin saluran Anda
2) Kirim /userbotjoinchannel di grup tertaut
3) Sekarang kirim perintah di grup tertaut

**Beberapa Command**

**◎› Memainkan Lagu 🎧**

• /play <nama lagu> : putar lagu yang Anda minta
• /play <url youtube> : Putar lagu melalui balasan url youtube
• /play <balas ke audio> : putar file balasan
• /dplay <nama lagu> : putar lagu yang Anda minta melalui deezer
• /splay <nama lagu> : putar lagu yang Anda minta melalui jio saavn

**◎› Playback ⏯**

• /player: buka panel pengaturan pemutar musik
• /skip: putar lagu berikutnya
• /pause: jeda pemutaran lagu
• /resume: melanjutkan pemutaran lagu
• /end: hentikan pemutaran musik
• /current: Tampilkan sedang diputar
• /playlist: Tampilkan daftar yang sedang diputar

*Cmd player dan semua cmd lain kecuali /play, /current dan /playlist hanya untuk admin grup*
""",
        
f"""
**◎› Putar Musik Di Channel 📮**

⚪️ Hanya untuk admin grup tertaut:

• /cplay [song name] - putar lagu yang Anda minta
• /cdplay [song name] - putar lagu yang Anda minta via deezer
• /csplay [song name] - putar lagu yang Anda minta via jio saavn
• /cplaylist - Perlihatkan daftar yang dimainkan
• /cccurrent - Perlihatkan yang diputar sekarang
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - lanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - stop pemutaran lagu
• /userbotjoinchannel - Undang asisten ke chat kamu

saluran Channel juga dapat digunakan sebagai pengganti c ( /cplay = /channelplay )

⚪️ Jika Anda tidak suka bermain di grup tertaut:

1) Dapatkan ID saluran Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Saluran dengan izin penuh
4) Tambahkan @{ASSISTANT_NAME} ke saluran sebagai admin.
5) Cukup kirim perintah di grup Anda.
""",

f"""
**◎› More Info 📲**

• /admincache: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
• /userbotjoin: Undang @{ASSISTANT_NAME} Userbot ke obrolan Anda

**◎› 📝 Command Khusus buat pengguna sudo**

 • /userbotleaveall - Keluarkan asisten musik dari semua obrolan chat
 • /gcast <reply to message> - global brodcast membalas pesan ke semua obrolan
 • /pmpermit [on/off] - enable/disable pesan pmpermit 
*Pengguna Sudo dapat menjalankan perintah apa pun di grup mana pun

◎› Owner Project: [Yunus Zend](https://t.me/ZendYNS)

"""
      ]
