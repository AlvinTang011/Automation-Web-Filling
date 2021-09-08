from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sys


# To install chrome driver manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Opens the webpage that we want to automate
web = webdriver.Chrome()
web.get('https://form.gov.sg/#!/5e3ebefa5203c3001108b7ba')

time.sleep(2)

# Change Your NRIC Accodringly
NRIC = "S8462840I"
nricPath = web.find_element_by_xpath('//*[@id="5e353dd16509040011d0333a"]')
nricPath.send_keys(NRIC)

# A Random Temperature Generated
a = random.randint(0, 9)
Temperature = str(a/10 + 36)
TemperaturePath = web.find_element_by_xpath('//*[@id="5e3541216509040011d0338b"]')
TemperaturePath.send_keys(Temperature)

# Your Email
Email = "tester@gmail.com"
EmailPath = web.find_element_by_xpath('//*[@id="5e9c34c3d273ec0011e23aef"]')
EmailPath.send_keys(Email)

# Submit the form
Submit = web.find_element_by_xpath('//*[@id="form-submit"]/div/button')
Submit.click()

time.sleep(3.5)

# Close the webpage
web.close()
driver.close()

# Close the terminal
sys.exit()
exit




