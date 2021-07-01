
EMAIL = 'satvikmittal638@gmail.com'
PWD = '#SNIPYsatvik'
import time
import os
import pandas as pd
import datetime
import smtplib
from plyer import notification

notification.notify(title="Birthday Wisher", message="Program Ran Successfully", timeout=4)
os.chdir("C:\\Users\\dmitt\\Desktop\\Projects\\Automatic Birthday Wisher\\")


def sendEmail(to, sub, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PWD)
    server.sendmail(EMAIL, to, f"Subject: {sub}\n\n{msg}")
    server.quit()


if __name__ == '__main__':
    data = pd.read_excel("data.xlsx")  # all birthday datas
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []  # to update the year in which we last wished him
    for index, item in data.iterrows():
        bday = item["Birthday"].strftime("%d-%m")
        # Only gives a list if comma is found b/w the values otherwise a string
        if today == bday and yearNow not in str(item['Year']):  # if the user hasn't been wished in the current year
            sendEmail(item["Email"], "Happy Birthday", item["Message"])
            writeInd.append(index)

    for i in writeInd:
        yearOld = data.loc[i, "Year"]
        data.loc[i, "Year"] = f"{yearOld}, {yearNow}"
    # prevents writing indices to the file
    data.to_excel("data.xlsx", index=False)  # writing the changes to the file
















