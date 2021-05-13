# Gmail elements
from datetime import datetime

gm_id = 'identifierId'
gm_id_next = 'identifierNext'
gm_pwd = '//*[@id="password"]/div[1]/div/div[1]/input'
gm_pwd_next = 'passwordNext'
gm_join_btn = 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt'
gm_chat = '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea'

# school site elements
schl_uname = '//*[@id="username"]'
schl_pwd = '//*[@id="password"]'
schl_login_btn = '//*[@id="user_login_btn"]'
schl_closePopup_btn = '/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/button'
schl_econnect = '/html/body/div[3]/div/div[1]/div/div[2]/div/ul/li[10]'

btnPos = 0
schl_startBTN = f"/html/body/div[3]/div/div[2]/div[2]/div/div[{btnPos}]/div[2]/div[3]"

# URLs and APIs
gmail_loginURL = 'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ'
BASE_URL = "https://api.telegram.org/bot"
Bot_API_TOKEN = "1723890890:AAFplWdIFchqVssA7sttfoxUd6Ar1aF4N94"
CHAT_ID = 1141858123

# Application Paths
browserPath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'


# BELL TIMINGS

def getTimeObj(myTime):
    return datetime.strptime(myTime, "%H:%M")


timings = [
    (getTimeObj("8:00"), getTimeObj("8:40")),
    (getTimeObj("8:50"), getTimeObj("9:30")),
    (getTimeObj("9:40"), getTimeObj("10:20")),
    (getTimeObj("10:40"), getTimeObj("11:20")),
    (getTimeObj("11:30"), getTimeObj("12:10")),
    (getTimeObj("12:20"), getTimeObj("1:00"))
]
