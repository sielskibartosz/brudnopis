import re
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def rgba_to_hex(rgba):
    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', rgba)
    if match:
        r, g, b = map(int, match.groups())
        return f'#{r:02x}{g:02x}{b:02x}'
    return None

driver = webdriver.Chrome()
wait = WebDriverWait(driver,3)

driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")

#menage cookies
try:
    accept_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '// *[ @ id = "L2AGLb"] / div'))
    )
    accept_button.click()
except TimeoutException:
    # Jeśli nie ma banera ciasteczek, po prostu idziemy dalej
    pass

email_search_box = driver.find_element(By.XPATH,'//*[@id="email"]')
email_search_box.send_keys("dupa@gmail.com")
password_search_box = driver.find_element(By.ID,'password')
password_search_box.send_keys("Pchelka")
password_search_box.send_keys(Keys.ENTER)
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="headingOne"]/button')
btn_color = button.value_of_css_property('background-color')
print(rgba_to_hex(btn_color))
print('#ccffce' == rgba_to_hex(btn_color))

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="collapseTwo"]/div/ul/li[1]/a')))
element.click()
time.sleep(2)
print("dupa")
dupa = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gender']")))
dupa.click()
# male_radio = driver.find_element(By.XPATH, "//div[label[text()='Male']]/input[@type='radio']")
# male_radio.click()
time.sleep(2)