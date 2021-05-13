from plyer import notification
import requests
from bs4 import BeautifulSoup  # used for web scraping


def notifyMe(title, msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon=None,
        timeout=3
    )


def getData(url):
    return requests.get(url).text


if __name__ == '__main__':
    # notifyMe("Satvik", "Hello there")
    soup = BeautifulSoup(getData("https://www.mohfw.gov.in/"), 'html.parser')
    print(getData("https://www.mohfw.gov.in/"))
    # for table in soup.find_all('tbody'):
    #     print(table)
