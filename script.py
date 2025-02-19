from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime

def capture_calendar_screenshot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        # 1) Access Discord’s login page.
        driver.get("https://discord.com/login")

        # 2) Wait for Discord page to load a bit longer, then take a screenshot of the QR code.
        for i in range(10, 0, -1):
            print(f"Waiting for Discord page to load: {i} seconds remaining")
            time.sleep(1)
        qr_screenshot = "discord_qr.png"
        driver.save_screenshot(qr_screenshot)
        print(f"QR code screenshot saved to {qr_screenshot}. Please open it to scan and log in.")

        # 3) Briefly wait again, giving more time for the login to complete.
        for i in range(20, 0, -1):
            print(f"Waiting for login to complete: {i} seconds remaining")
            time.sleep(1)

        # 3.5) Attempt to find and click the "Authorize" button if it appears.
        try:
            authorize_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Authorize")]'))
            )
            authorize_button.click()
            print("Clicked the authorize button. Waiting 10 seconds...")
            time.sleep(10)
        except:
            print("No authorize button found or not clickable. Continuing...")

        # 4) After you're logged in, go to the Raid Helper calendar page.
        driver.get("https://raid-helper.dev/calendar/1288597337979228190")
        for i in range(5, 0, -1):
            print(f"Waiting for calendar to load: {i} seconds remaining")
            time.sleep(1)

        # 5) Take the final screenshot.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"calendar_screenshot_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Calendar screenshot saved to {screenshot_path}")
        return screenshot_path

    finally:
        driver.quit()

if __name__ == "__main__":
    capture_calendar_screenshot()