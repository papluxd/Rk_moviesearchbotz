# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''Hᴇʏ! {} 😅,

Mᴇ! Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ.🤖

I Cᴀɴ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇꜱ Fᴏʀ Yᴏᴜ.🔍

Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ

@Rk_botowner

''')
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/99e311290ec06486bcc8f.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", '''ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ,
ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 1800))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, i ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.✅

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @Rk_botowner''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''How to get movies & series from Bot
♻️ 𝖳ɪᴘ ᴛᴏ ᴜ𝗌ᴇ ʙᴏᴛ : ᴅᴏɴ'ᴛ ɪɴᴄʟᴜᴅᴇ ᴀɴʏᴛʜɪɴɢ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ. 

𝖤ɢ: 𝖫ᴜᴄɪғᴇʀ 𝖲𝟶𝟷𝖤𝟶𝟻 ✅

𝖫ᴜᴄɪғᴇʀ 𝖲ᴇᴀ𝗌ᴏɴ 𝟷 𝖤ᴘɪ𝗌ᴏᴅᴇ 𝟻 ❌

𝖡ʟᴀᴄᴋ 𝖶ɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 ✅

𝖡ʟᴀᴄᴋ ᴡɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 𝖧ɪɴᴅɪ ❌

𝖡ʟᴀᴄᴋ𝖶ɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 ❌

○ 𝖨ғ 𝖬ᴏᴠɪᴇ / 𝖲ᴇʀɪᴇ𝗌 𝖭ᴏᴛ 𝖥ᴏᴜɴᴅ 𝖳ʜᴇɴ 𝖱ᴇǫᴜᴇ𝗌ᴛ 𝖨ɴ 𝖦ɪᴠᴇɴ 𝖥ᴏʀᴍᴀᴛ 𝖮ɴʟʏ

👉🏼 𝖭ᴀᴍᴇ | 𝖸ᴇᴀʀ | 𝖱ᴇ𝗌ᴏʟᴜᴛɪᴏɴ | 𝖫ᴀɴɢᴜᴀɢᴇ''')
