
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    driver.get("https://google.com")
    # // *[ @ id = "L2AGLb"] / div
    try:
        accept_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '// *[ @ id = "L2AGLb"] / div'))
        )
        accept_button.click()
    except TimeoutException:
        # Jeśli nie ma banera ciasteczek, po prostu idziemy dalej
        pass


    search__box = driver.find_element(by=By.XPATH, value='//*[@name="q"]')
    search__box.send_keys("selenium")
    search__box.submit()
    result = wait.until(EC.presence_of_element_located((By.ID, "search")))
    assert result.text != ""
