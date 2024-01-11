import requests
from bs4 import BeautifulSoup

from selenium import webdriver #used for collecting data from dynamic setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains #allow hovering over item


# Set up Chrome options
"""chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_path = '/path/to/chromedriver'

# Set up driver
driver = webdriver.Chrome(options=chrome_options, executable_path=webdriver_path)"""

url = 'https://ptable.com/'

#Must allow "Allow Remote Automation" in Safari Settings
driver = webdriver.Safari() # if using Safari
driver.get(url)

##giving time for page to load
wait = WebDriverWait(driver, 10)
#electroneg_radio = wait.until(EC.element_to_be_clickable((By.ID, 't_electroneg')))
#electroneg_radio.click()
#time.sleep(5)

element_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-atomic]')))

particle = {}
# Extract and store the data in the dictionary
for item in element_items:
    element_details = {}

    #Atomic number 
    atomic_number = item.get_attribute('data-atomic')

    #Atomic mass
    atomic_weight_element = item.find_element(By.TAG_NAME, 'data')
    element_details['Atomic_mass'] = atomic_weight_element.text if atomic_weight_element else "Not Found"
    
    #Element Name:
    element_name_element = item.find_element(By.TAG_NAME, 'em')
    element_name = element_name_element.text if element_name_element else "Unknown"
    element_details['Atomic_number'] = atomic_number

    #Electronegatitivity    
    """    try:
        # Locate the <output> tag that contains the electronegativity value
        electronegativity_element = item.find_element(By.XPATH, './/following-sibling::output')
        electronegativity = electronegativity_element.text.strip() if electronegativity_element else "Not Available"
    except Exception as e:
        electronegativity = "Not Available"

    element_details['Electronegativity'] = electronegativity"""

    #Dictionary of all elements
    particle[element_name] = element_details

# Close the browser
driver.quit()

def get_elementInfo(elementName):
    atom = particle[elementName]
    return atom
def get_elementMass(elementName):
    atom = particle[elementName]
    atomMass = atom['Atomic_mass']
    return atomMass

def get_electronegativity(elementName):
    if True:
        return None 
    atom = particle[elementName]
    atomElectro = atom['Electronegativity']
    return atomElectro


#testing
"""particle1 = particle["Hydrogen"]
print(particle1)
particle1Mass = particle1["Atomic_mass"]
print(particle1Mass)"""
particle1 = get_elementInfo("Hydrogen")
print(particle1)
particle1Mass = get_elementMass("Hydrogen")
print(f'This is the mass of Hydrogen: {particle1Mass}')
particleElectro = get_electronegativity("Hydrogen")
print(f"Electronegativity of Hydrogen is: {particleElectro}")
print(f"printing all stored data:\n {particle}")