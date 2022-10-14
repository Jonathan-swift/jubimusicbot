import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26515107"))
    API_HASH = os.environ.get("API_HASH", "71c39ddb9da42a66087c3b4cf57e21c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5714189559:AAGjeaACKdgplyIbEZ5BbqM3iidTC61PCB8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7MUgzLGmnsDmmR3lgIh+AgNhl/W+yO1Gg7ToYtVIuRFbu6ymHl1xVTiv/MUs84fZgMt0cpMpE0OcEi7EBehvNAvyGokg/zOHz6JLt/EiOv6c+1EkXGecjDKKne8EzUxQE66hEy6niYYg2nZcll3VM7CZ4/tCb9+OKO8gQKFQBOFrG96gemXcqJigsV3DNofA/ALwlg/fR1OyrXoeUx3MgPNScdEYIQURIuuk51P0yLzTVVSz/3y5k/hfwjCOMqNQqw17cmKkFgPWoLvJRNnlV7TLNVzx6QW/zHuywdtCwyrsOdaLPusCQw4UMDo//ulrRGxVtT51r306UiVKmdj4bVw==")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Jubis_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "jubistalk") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "jonathaan_swift") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5519737346")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
