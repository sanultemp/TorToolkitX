try:
    from .ExecVars import ExecVars
except:

    class ExecVars:
        # Set true if its VPS
        IS_VPS = True

        API_HASH = "4d4023337b8cc46c306af69adb5fc21a"
        API_ID = 7469109
        BOT_TOKEN = "5078521431:AAHDz1_5lJYjugyXDCLdtSbeuEuUxxdMLcA"
        BASE_URL_OF_BOT = ""

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [2118362497, -1001516237874]
        OWNER_ID = 0

        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = False

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1700000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DATABASE_URL = (
            "postgres://xiqfwupvokveje:237bc1d5fad9a3180a6fa351cf4c816bcb0ae883d7df6658d499aef59799d403@ec2-34-194-14-176.compute-1.amazonaws.com:5432/dfqe18923io1s2"
        )

        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        # DATABASE_URL = "dbname=tortk user=postgres password=your-pass host=db port=5432"

        # MEGA CONFIG
        MEGA_ENABLE = False
        MEGA_API = ""
        MEGA_UNAME = None
        MEGA_PASS = None

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"
        
        # Instagram Credentials Stuff [( if you want InstaDL to work :)]
        INSTA_UNAME = ""
        INSTA_PASS = ""

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 20

        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # Custom Trackers for QBT..
        ADD_CUSTOM_TRACKERS = True
        TRACKER_SOURCE = "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = ""

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 20

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50, 10, 2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
