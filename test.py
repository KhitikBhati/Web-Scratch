from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/home/somesh/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.airtel.in/myplan-infinity/')

time.sleep(5)

dict={
    "plan1":"",
    "plan2":"",
    "plan3":"",
    "plan4":"",
    "plan5":""
}

for i in range(1,5):
    print(driver.find_elements(By.XPATH,'//*[@id="root"]/div/div/div[1]/div[1]/div[2]/section/div/div[1]/div'+'['+str(i)+']')[0].text)
    dict['plan'+str(i)]=driver.find_elements(By.XPATH,'//*[@id="root"]/div/div/div[1]/div[1]/div[2]/section/div/div[1]/div'+'['+str(i)+']')[0].text

json_object = json.dumps(dict, indent=4)

fileName="AirtelPlans.json"

with open(fileName, "w") as outfile:
        outfile.write(json_object)


driver.quit()