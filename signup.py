'''!pip install selenium
!sudo mv -f chromedriver /usr/local/bin/chromedriver'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
from exceptions import Checks as testudo
def get_options():
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        return options
def sign_up_special(driver, xpath):
        # Click on add to __ and then click ok on message that pops up
        length = len(driver.find_elements(By.TAG_NAME, 'tr')) #can't access new tr's until loaded so we do this + 2
        driver.find_element(By.XPATH, f'//tr[{length + 2}]/td//div[2]/button').click()
        driver.find_element(By.XPATH, f'//tr[{length + 2}]/td/div/div/div/div[2]/button').click()
        curr = driver.find_elements(By.XPATH, xpath)
        try:
                curr = curr[:6]
        except IndexError:
                curr = curr[:len(curr)]
        for k in curr:
                k.click()
        driver.find_element(By.XPATH, f'//table/tbody/tr[{length + 2}]/td//div[3]/button').click()
if  __name__ == "main":

        student_classes = ['AASP100']
        sections = ['0301']

        url = "https://testudo.umd.edu/"

        testudo.is_Testudo_down()

        options = get_options()

        driver = webdriver.Chrome(options= None)
        driver.get(url)
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Registration').click()

        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(5)
        username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('UNAME')
        password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('PWORD')
        driver.find_element(By.NAME, '_eventId_proceed').click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'nav_button'))) # Will this also give time for user to authenticate?
        driver.find_element(By.XPATH, '//*[@id="nav_button"]/div/span[1]').click()
        driver.find_element(By.XPATH, '//*[@id="Registration - Drop/Add"]').click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'drop-add-term-selector'))) # Will this also give time for user to authenticate?
        classes = driver.find_element(By.CLASS_NAME, 'drop-add-term-selector')
        semesters = classes.find_elements(By.TAG_NAME, "button")
        semesters_modified = [f"{i} : {semesters[i].text}" for i in range(len(semesters))]
        print(semesters_modified)
        found = False
        while not found:
                try:
                        #semester = int(input("Which semester do you want to register for?"))
                        classes.find_element(By.XPATH, f"//button[.= 'Spring 2022']").click() #{semesters[semester].text}
                        found = True
                except IndexError:
                        print("Enter a number in the range")
                        continue

        # What if there are multiple sessions?
        maincontent = driver.find_element(By.ID, 'mainContent')
        no_multiple_session = False
        time.sleep(2)
        try:
                maincontent.find_element(By.XPATH, '//div[2]/button').click()
        except NoSuchElementException:
                no_multiple_session = True




        #Find All input boxes
        for i in range(len(student_classes)): #want to add all the classes in the arrays
                input_box = driver.find_element(By.ID, 'crs_pending')
                saved_boxes = input_box.find_elements(By.TAG_NAME, "input")
                saved_boxes.pop() # we dont care about the number of credits
                saved_boxes[0].send_keys(student_classes[i])
                saved_boxes[1].send_keys(sections[i])
                maincontent = driver.find_element(By.TAG_NAME, 'form')
                maincontent.find_elements(By.TAG_NAME, 'button')[-2].click() #This is the submit button because the buttons before this are edit/drop and view schedule is after
                #Holdfile
                try:
                        element = maincontent.find_element(By.XPATH, '//table/tbody')
                        if('Non-Standard' in maincontent.text):
                                ele = driver.find_element(By.XPATH, '//*[@id="drop_add_form"]/table/tbody')
                                tr = ele.find_elements(By.TAG_NAME, 'tr')[-1] #want to get the last element because we want to click only that
                                tr.find_element(By.TAG_NAME, 'button').click()
                        else:
                                sign_up_special(element, '//*[starts-with(@id, "openSectionCheckbox_")]')
                except NoSuchElementException:
                        continue


