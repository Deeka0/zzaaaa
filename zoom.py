from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from random import randint
import csv, re, time

#from selenium.webdriver.safari.options import Options
# from os.path import abspath

nameFile = open(r"/Users/dark/Desktop/zzAll/names.csv", 'r')
nameDict = csv.DictReader(nameFile, delimiter=',')
nameList = []
for row in nameDict:
    nameList.append(row)

detailsFile = open(r"/Users/dark/Desktop/zzAll/details.csv", 'r')
detailsDict = csv.DictReader(detailsFile, delimiter=',')
for row in detailsDict:
    detailsDict = row

if detailsDict['webinar'] == 'yes':
    url = 'https://us06web.zoom.us/wc/join/' + str(detailsDict['meetingID']) + '?pwd=' + str(detailsDict['password'])
else:
    url = 'https://us05web.zoom.us/wc/join/' + str(detailsDict['meetingID']) + '?pwd=' + str(detailsDict['password'])


def join(url):
    options = Options()
    options.headless = False
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get(url)
    time.sleep(2)
    title = driver.title
    if ("Zoom" or "Meeting" or "Room") in title:
        try:
            text_box = driver.find_element(by=By.NAME, value="inputname")
            submit_button = driver.find_element(by=By.ID, value="joinBtn")
            name = str(nameList[randint(0, len(nameList))]['names']).capitalize()
            text_box.send_keys(name)
            time.sleep(1)
            submit_button.click()
            if 'Zoom meeting on web - Zoom' == driver.title:
                email_box = driver.find_element(by=By.NAME, value="inputemail")
                join_button = driver.find_element(by=By.ID, value="joinBtn")
                email = re.sub('[\s+]', '', name) + str(randint(1, 100000)) + '@yev.me'
                time.sleep(3)
                email_box.send_keys(email)
                join_button.click()
                
            if 'Error' in driver.title:
                print('This meeting link is expired or invalid')
                driver.quit()
                return 'This meeting link is expired or invalid'
            else:
                time.sleep(5)
                next_join_btn = driver.find_element(by=By.CLASS_NAME, value="preview-join-button")
                next_join_btn.click()

                print('Joined meeting')
                time.sleep(11000)
                driver.quit()
                return 'Joined meeting'

        except NoSuchElementException:
            print('Error! The page might have been changed')
            driver.quit()
            return
    else:
        print('Error! The page might have been changed')
        driver.quit()
        return

join(url)

