from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os


def test_ui_load():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("http://127.0.0.1:5000")
    time.sleep(2)

    assert "Resume" in driver.page_source

    driver.quit()


def test_file_upload():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("http://127.0.0.1:5000")
    time.sleep(2)

    file_input = driver.find_element(By.ID, "fileInput")
    button = driver.find_element(By.TAG_NAME, "button")

    file_path = os.path.abspath("sample.pdf")

    file_input.send_keys(file_path)
    button.click()

    time.sleep(3)

    assert "Recommended Jobs" in driver.page_source

    driver.quit()
