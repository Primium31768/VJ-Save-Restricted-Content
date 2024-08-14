import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27868202"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bf6d423ddc4a4999f09750872bdc2497")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://adultverse04:adultverse04@adultverse04.wpltj.mongodb.net/?retryWrites=true&w=majority&appName=adultverse04")
