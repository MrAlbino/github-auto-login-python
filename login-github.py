from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

driver = webdriver.Chrome()
users=[]

with open("user.txt","r") as file:
    users=file.readlines()

user=users[0].split(",")
user=user[0].split(" ")
url="https://github.com/login"

driver.get(url)

input_text=driver.find_element_by_xpath("//*[@id='login']/form/div[4]/label[1]")

input_text=driver.find_element_by_xpath("//*[@id='login']/form/div[4]/label[2]")
girdi=user[0]
girdi1=user[1]

send_input1=driver.find_element_by_id("password")
send_input=driver.find_element_by_id("login_field")

send_input.send_keys(girdi)

send_input1.send_keys(girdi1)

time.sleep(3)

submit=driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]")

submit.click()

time.sleep(6)

dropdown=driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary")

dropdown.click()
time.sleep(1)

sign_out=driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/form/button")

ActionChains(driver).move_to_element(sign_out).click(sign_out).perform() 

time.sleep(4)

driver.close()
