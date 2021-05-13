import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import RESOURCES

from telegram.ext import Updater
from PIL import ImageGrab


class AutomateSchool:
    updater = Updater(token=RESOURCES.Bot_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    bot = dispatcher.bot

    def __init__(self, schoolURL, uname, pwd, classLen):
        chromeOpt = Options()
        chromeOpt.binary_location = RESOURCES.browserPath
        chromeOpt.add_argument("--disable-blink-features=AutomationControlled")
        chromeOpt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })

        self.schoolURL = schoolURL
        self.uname = uname
        self.pwd = pwd
        self.classLen = classLen
        self.chromeDriver = webdriver.Chrome("chromedriver.exe", options=chromeOpt)
        self.chromeDriver.maximize_window()

    # School site functions:
    def loginToSchoolSite(self):
        time.sleep(1)
        self.chromeDriver.get(self.schoolURL)

        uname_elem = self.chromeDriver.find_element_by_xpath(RESOURCES.schl_uname)
        uname_elem.click()
        uname_elem.send_keys(self.uname)

        pwd_elem = self.chromeDriver.find_element_by_xpath(RESOURCES.schl_pwd)
        pwd_elem.click()
        pwd_elem.send_keys(self.pwd)

        self.chromeDriver.find_element_by_xpath(RESOURCES.schl_login_btn).click()
        AutomateSchool.bot.send_message(text="Successfully logged in to the school site", chat_id=RESOURCES.CHAT_ID)

    def goToEconnect(self):
        try:
            self.chromeDriver.find_element_by_xpath(RESOURCES.schl_closePopup_btn).click()
        except Exception as e:
            print(e)
        time.sleep(1)
        self.chromeDriver.find_element_by_xpath(RESOURCES.schl_econnect).click()
        AutomateSchool.bot.send_message(text="Opened E-connect", chat_id=RESOURCES.CHAT_ID)

    def clickStartBTN(self):
        clickedBTN = False
        while not clickedBTN:
            for i in range(3, 9):
                try:
                    RESOURCES.btnPos = i
                    self.chromeDriver.find_element_by_xpath(RESOURCES.schl_startBTN).click()
                    clickedBTN = True
                except Exception as e:
                    print("Start button not found")
                    # self.chromeDriver.refresh()
        return clickedBTN

    def exitClass(self):
        self.chromeDriver.close()

    # Google Meet functions:
    def signInToGmail(self, email, pwd):
        self.chromeDriver.get(RESOURCES.gmail_loginURL)
        self.chromeDriver.find_element_by_id(RESOURCES.gm_id).send_keys(email)  # input email
        self.chromeDriver.find_element_by_id(RESOURCES.gm_id_next).click()  # click next
        self.chromeDriver.implicitly_wait(10)

        self.chromeDriver.find_element_by_xpath(RESOURCES.gm_pwd).send_keys(pwd)  # input pwd
        self.chromeDriver.find_element_by_id(RESOURCES.gm_pwd_next).click()  # click next
        self.chromeDriver.implicitly_wait(10)

        AutomateSchool.bot.send_message(text="Gmail Login Successful", chat_id=RESOURCES.CHAT_ID)

    def turnOffMicAndCam(self):
        time.sleep(1)
        self.chromeDriver.switch_to.window(self.chromeDriver.window_handles[1])
        self.chromeDriver.find_element_by_tag_name('body').send_keys("CTRL", 'd')
        self.chromeDriver.find_element_by_tag_name('body').send_keys("CTRL", 'e')
        AutomateSchool.bot.send_message(text="Mic and Cam turned off", chat_id=RESOURCES.CHAT_ID)

    def joinMeet(self):
        self.chromeDriver.find_element_by_css_selector(RESOURCES.gm_join_btn).click()
        AutomateSchool.bot.send_message(text="Class joined successfully !!", chat_id=RESOURCES.CHAT_ID)

    def sendMsgInChat(self, msg):
        self.chromeDriver.find_element_by_tag_name('body').send_keys("CTRL", "ALT", "c")
        chat = self.chromeDriver.find_element_by_xpath(RESOURCES.gm_chat)
        chat.click()
        chat.send_keys(msg)
        AutomateSchool.bot.send_message("Sent", msg, "in the chat")

    @staticmethod
    def sendCurrentScreenshot():
        ImageGrab.grab().save("screenshotClassSuccess.png")
        AutomateSchool.bot.sendPhoto(photo=open("screenshotClassSuccess.png", "rb"),
                                     caption="Here is the current screenshot",
                                     chat_id=RESOURCES.CHAT_ID)
