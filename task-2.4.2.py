from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_css_selector("button.btn")
# говорим Selenium проверять в течение 12 секунд, пока стоимость не станет $100
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button.click()

x = browser.find_element_by_css_selector("#input_value").text
input = browser.find_element_by_css_selector('.form-control')
input.send_keys(calc(x))

button = browser.find_element_by_css_selector("#solve")
button.click()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text