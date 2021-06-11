import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "TeamKingUserbot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/27106d0e7ab86b2d0a929.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MightKing Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "KingUserbotSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "Vc MusicINDO")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Yunus-ZEND/VC-MusicINDO")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", None)
OWNER_USERNAME = getenv ("OWNER_USERNAME", "ZendYNS")

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
