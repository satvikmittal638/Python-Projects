from AutomateSchool import AutomateSchool
import RESOURCES
from datetime import datetime as timing
import time

if __name__ == '__main__':

    obj = AutomateSchool("https://dpsharidwar.edunexttech.com/Index", "yourAdmnNo", "pwd", 40)

    obj.signInToGmail("your.email@dpshardwar.com", "pwd")
    obj.loginToSchoolSite()
    obj.goToEconnect()

    while 8 <= timing.now().hour <= 13:
        if obj.clickStartBTN():
            time.sleep(2)
            obj.turnOffMicAndCam()
            obj.joinMeet()
            obj.sendCurrentScreenshot()
            time.sleep(obj.classLen * 60)
            obj.exitClass()

    AutomateSchool.bot.send_message(text="School ended successfully", chat_id=RESOURCES.CHAT_ID)
    print("School ended")
