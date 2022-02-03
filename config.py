#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "5087927386:AAEx7kS8Rpj15H6xpXtyeW3VGerTucoj_mo") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "1976680")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "9073255ce64a6072a59099803493f97d") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "1940030638")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # Get from MongoDB Atlas

