import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "MusicVirChannel")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/b1e5da058a63a52ec8265.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ram")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "MusicVirGroup")
PROJECT_NAME = getenv("PROJECT_NAME", "Vir Project")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/farizjr1/VIR-MUSIC-INDO")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", None)
OWNER_USERNAME = getenv ("OWNER_USERNAME", "farizjlr")

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
