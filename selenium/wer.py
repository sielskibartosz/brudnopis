from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    # Uruchom przeglądarkę (tutaj Chrome, wymaga chromedriver)
    driver = webdriver.Chrome()

    try:
        # Otwórz Google
        driver.get("https://www.google.com")

        # Znajdź pole wyszukiwania
        search_box = driver.find_element(By.NAME, "q")

        # Wpisz "python" i naciśnij Enter
        search_box.send_keys("python" + Keys.RETURN)

        # Poczekaj aż pojawią się wyniki (elementy z id="search")
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Sprawdź, czy wyniki faktycznie się pojawiły (czyli jest jakiś tekst w elemencie)
        assert results.text != "", "Brak wyników wyszukiwania"

    finally:
        driver.quit()
