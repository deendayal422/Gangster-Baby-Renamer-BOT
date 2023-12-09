import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16681004")

API_HASH = os.environ.get("API_HASH", "161b61f5a06dd299a3d88a3384b9f104")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6914510071:AAFgosVOYU_Z67T99cgfKLMmeE31DkpSwrA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://dndldhkd:iZgn69Q8PIN28EER@cluster0.mgz6put.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/2a78470d2e9439d52fe15.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6646028262').split()]

PORT = os.environ.get("PORT", "8080")
