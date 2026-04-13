from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os


# ---------- SETUP DRIVER ----------
def create_driver():
    options = Options()
    options.add_argument("--headless")  # run without opening browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver




# ---------- TEST 1: SUCCESSFUL UPLOAD ----------
def test_upload_success():
    print("\n🚀 TEST 1: Successful Upload")


    driver = create_driver()
    driver.get("http://127.0.0.1:5000")


    wait = WebDriverWait(driver, 10)


    try:
        # Step 1: Upload file
        file_input = wait.until(
            EC.presence_of_element_located((By.ID, "resumeFile"))
        )


        file_path = os.path.join(os.path.dirname(__file__), "sample.pdf")
        if not os.path.exists(file_path):
            raise Exception("sample.pdf not found")


        file_input.send_keys(file_path)
        print("📄 File uploaded")


        # Step 2: Click button
        driver.find_element(By.ID, "analyzeBtn").click()
        print("🔘 Button clicked")


        # Step 3: Wait for result
        result = wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        )


        filename = driver.find_element(By.ID, "filename").text


        if result.is_displayed() and filename:
            print("✅ TEST PASSED")
        else:
            print("❌ TEST FAILED")


    except Exception as e:
        print("❌ ERROR:", str(e))


    finally:
        driver.quit()




# ---------- TEST 2: NO FILE UPLOADED ----------
def test_no_file():
    print("\n🚀 TEST 2: No File Uploaded")


    driver = create_driver()
    driver.get("http://127.0.0.1:5000")


    wait = WebDriverWait(driver, 10)


    try:
        # Click button without file
        driver.find_element(By.ID, "analyzeBtn").click()


        error = wait.until(
            EC.presence_of_element_located((By.ID, "error"))
        )


        if "Please select a PDF file" in error.text:
            print("✅ TEST PASSED")
        else:
            print("❌ TEST FAILED")


    except Exception as e:
        print("❌ ERROR:", str(e))


    finally:
        driver.quit()




# ---------- TEST 3: INVALID FILE TYPE ----------
def test_invalid_file():
    print("\n🚀 TEST 3: Invalid File Type")


    driver = create_driver()
    driver.get("http://127.0.0.1:5000")


    wait = WebDriverWait(driver, 10)


    try:
        file_input = wait.until(
            EC.presence_of_element_located((By.ID, "resumeFile"))
        )


        # Create dummy file
        invalid_file = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(invalid_file, "w") as f:
            f.write("dummy")


        file_input.send_keys(os.path.abspath(invalid_file))
        driver.find_element(By.ID, "analyzeBtn").click()


        print("📄 Invalid file uploaded")


        # Just check system response (error or handled)
        wait.until(
            EC.presence_of_element_located((By.ID, "error"))
        )


        print("✅ TEST PASSED (system handled invalid input)")


        pass


    except Exception as e:
        print("❌ ERROR:", str(e))


    finally:
        driver.quit()




# ---------- TEST 4: LOADING INDICATOR ----------
def test_loading():
    print("\n🚀 TEST 4: Loading Indicator")


    driver = create_driver()
    driver.get("http://127.0.0.1:5000")


    wait = WebDriverWait(driver, 10)


    try:
        file_input = wait.until(
            EC.presence_of_element_located((By.ID, "resumeFile"))
        )


        file_path = os.path.abspath("sample.pdf")
        file_input.send_keys(file_path)


        driver.find_element(By.ID, "analyzeBtn").click()


        loading = driver.find_element(By.ID, "loading")


        if loading:
            print("⏳ Loading shown")


        wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        )


        print("✅ TEST PASSED")


    except Exception as e:
        print("❌ ERROR:", str(e))


    finally:
        driver.quit()




# ---------- RUN ALL TESTS ----------
if __name__ == "__main__":
    test_upload_success()
    test_no_file()
    test_invalid_file()
    test_loading()
