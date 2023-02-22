from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from random import randint
import csv, re, time


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
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.page_load_strategy = 'eager'
    driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(60)
    wait = WebDriverWait(driver, timeout=15, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
    driver.get(url)
    if "Zoom meeting on web - Zoom" == driver.title:
        try:
            text_box = driver.find_element(By.NAME, "inputname")
            first_join_button = driver.find_element(By.ID, "joinBtn")
            name = str(nameList[randint(0, len(nameList))]['names']).capitalize()
            text_box.send_keys(name)
            first_join_button.click()
            if 'Zoom meeting on web - Zoom' == driver.title:
                email_box = driver.find_element(By.NAME, "inputemail")
                second_join_button = driver.find_element(By.ID, "joinBtn")
                email = re.sub('[\s+]', '', name) + str(randint(1, 100000)) + '@yev.me'
                email_box.send_keys(email)
                second_join_button.click()

            third_join_btn = driver.find_element(by=By.CLASS_NAME, value="preview-join-button")
            third_join_btn.click()

            join_audio_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[11]/div[3]/div/div[2]/div/button")))
            join_audio_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[11]/div[3]/div/div[2]/div/button")
            join_audio_btn.click()

            print('Joined meeting')
            time.sleep(11000)
            leave_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/footer/div[1]/div[3]/button")
            leave_button.click()
            confirm_leave_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/footer/div[2]/div[2]/div/div/button")
            confirm_leave_button.click()
            print("User meeting timeout is reached, please re-run program to create user")
            time.sleep(10)
            driver.quit()
                
            if 'Error' in driver.title:
                print('This meeting link is expired or invalid')
                driver.quit()
                return 'This meeting link is expired or invalid'

        except NoSuchElementException:
            print('Error! Please check your internet connection')
            driver.quit()
            return
    else:
        print('Error! The page might have been changed')
        driver.quit()
        return

join(url)

