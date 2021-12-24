'''!pip install selenium
!sudo mv -f chromedriver /usr/local/bin/chromedriver'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

student_classes = ['AASP100']
sections = ['0301']

url = "https://testudo.umd.edu/"


options = Options()
options.headless = True

driver = webdriver.Chrome(options= None)
driver.get(url)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Registration').click()

driver.switch_to.window(driver.window_handles[-1])
driver.implicitly_wait(5)
username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('USERNAME')
password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('PASSWORD')
driver.find_element(By.NAME, '_eventId_proceed').click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'nav_button')))
driver.find_element(By.XPATH, '//*[@id="nav_button"]/div/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="Registration - Drop/Add"]').click()
maincontent = driver.find_element(By.ID, 'mainContent')
classes = driver.find_element(By.CLASS_NAME, 'drop-add-term-selector')
semesters = classes.find_elements(By.TAG_NAME, "button")
semesters_modified = [f"{i} : {semesters[i].text}" for i in range(len(semesters))]
print(semesters_modified)
found = False
while not found:
        try:
                semester = int(input("Which semester do you want to register for?"))
                classes.find_element(By.XPATH, f"//button[.= '{semesters[semester].text}']").click()
                found = True
        except IndexError:
                print("Enter a number in the range")
                continue
# What if there are multiple sessions?
no_multiple_session = False
try:
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/button').click()
except NoSuchElementException:
        no_multiple_session = True

#Find All input boxes
input_box = driver.find_element(By.ID, 'crs_pending')
saved_boxes = input_box.find_elements(By.TAG_NAME, "input")
saved_boxes.pop() # we dont care about the number of credits
saved_boxes[0].send_keys(student_classes[0])
saved_boxes[1].send_keys(sections[0])

#need to add cases for holdfile and waitlist 
