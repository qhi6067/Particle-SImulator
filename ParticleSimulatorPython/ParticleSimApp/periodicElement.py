import requests
from bs4 import BeautifulSoup

from selenium import webdriver #used for collecting data from dynamic setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_path = '/path/to/chromedriver'

# Set up driver
driver = webdriver.Chrome(options=chrome_options, executable_path=webdriver_path)

url = 'https://ptable.com/'

#Must allow "Allow Remote Automation" in Safari Settings
#driver = webdriver.Safari() # if using Safari
driver.get(url)

##giving time for page to load
wait = WebDriverWait(driver, 10)

element_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-atomic]')))

particle = {}
# Extract and store the data in the dictionary
for item in element_items:
    element_details = {}
    atomic_number = item.get_attribute('data-atomic')
    atomic_weight_element = item.find_element(By.TAG_NAME, 'data')
    element_details['Atomic_mass'] = atomic_weight_element.text if atomic_weight_element else "Not Found"
    element_name_element = item.find_element(By.TAG_NAME, 'em')
    element_name = element_name_element.text if element_name_element else "Unknown"
    element_details['Atomic_number'] = atomic_number
    
    particle[element_name] = element_details

# Close the browser
driver.quit()

#testing
particle1 = particle["Hydrogen"]
print(particle1)