from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver, 10)

        # Kliknij zgodę na cookies, jeśli się pojawi
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Zaakceptuj wszystko']"))
            )
            consent_button.click()
        except:
            print("Brak zgody cookies — kontynuuję")

        # Poczekaj, aż pole wyszukiwania będzie widoczne i interaktywne
        search_box = wait.until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )

        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)

        # Poczekaj na zmianę tytułu strony
        wait.until(EC.title_contains("Selenium"))

        assert "Selenium" in driver.title

    finally:
        driver.quit()
