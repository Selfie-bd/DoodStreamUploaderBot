#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "5194035154:AAE_IlC8CNAycbtFQpQx6z-Ys1eQMoyLsiU") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "2904321")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "87faa32f68324a09aecdd9911db846a2") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "1906359620")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

