from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")  
service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password, and login button elements
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password, and clock the button
username_field.send_keys('pythonstudent')
password_field.send_keys('PythonStudent123$')
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Test Box
elements = (WebDriverWait(driver, 10).
            until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]'))))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the from fields and submitt button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')


# Fill in the form fields
fullname_field.send_keys('Automation Test')
email_field.send_keys('automation@gmail.com')
current_address_field.send_keys('123 Automation St, Test City, TX')
permanent_address_field.send_keys('456 Permanent Ave, Test City, TX')
driver.execute_script("arguments[0].click();", submit_button)

input("Press Enter to close the browser")
driver.quit()
