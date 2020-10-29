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
    BOT_TOKEN = "1070013851:AAFOZo76ZzpfKGOuCJ8bKBmPkP-2FOhJWeQ"
    DATABASE_URL = "postgres://ilnpklfnmolbdw:5c45f41fb64a2d46f7890af8c8454d101cc3e286c257078d184a68621f488f18@ec2-52-44-235-121.compute-1.amazonaws.com:5432/dc4l0h6oida2mooida2mo"
    APP_ID = "1948374"
    API_HASH = "113be69e13bf6f71583fb0783b1ab841"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**p [{}](tg://user?id={})**\n__rusak"
