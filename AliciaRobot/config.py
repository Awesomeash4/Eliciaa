# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/AliciaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2857558  # integer value, dont use ""
    API_HASH = "1038be815e038592fa2b483c13dd6c4b"
    TOKEN = "1613196478:AAHzs8A_73OkOBISpQ5emx5ToDxMlJu0XmU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1212368262  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "H1M4N5HU0P"
    SUPPORT_CHAT = "MafiaBot_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001204088829
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001459323267
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://vhyrades:gOlW9HnB8gjo80BKZMKLdQucme9Si2nB@fanny.db.elephantsql.com/vhyrades" # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = "https://aliciarobot.herokuapp.com/"
    SPAMWATCH_API = "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    MONGO_DB_URI = "mongodb+srv://AliciaRobotOP:AliciaRobotOP@cluster0.pfhfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    BOT_ID = 1613196478
    TEMP_DOWNLOAD_DIRECTORY = "./"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

