# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLab4Group2side:
    def setup_method(self, method):
        # Initialize WebDriver for Firefox
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # Set implicit wait
        self.vars = {}

    def teardown_method(self, method):
        # Quit WebDriver
        self.driver.quit()

    def clear_and_enter_text(self, by, selector, text):
        """Clears an input field and enters the provided text."""
        element = self.driver.find_element(by, selector)
        element.clear()
        time.sleep(1)  # Pause for visibility
        element.send_keys(text)

    def test_body_fat_calculator_with_logic(self):
        # Navigate to Body Fat Calculator
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")
        self.driver.set_window_size(1753, 945)

        wait = WebDriverWait(self.driver, 10)  # Explicit wait

        # Pause to allow the page to load fully
        time.sleep(1)

        # Gender selection: Set "female" or "male"
        gender = "female"

        if gender == "female":
            # Select Gender: Female
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark"))).click()
            time.sleep(1)

            # Fill Female Inputs
            self.clear_and_enter_text(By.NAME, "cage", "30")  # Age
            self.clear_and_enter_text(By.NAME, "cweightkgs", "55")  # Weight in kg
            self.clear_and_enter_text(By.ID, "cheightmeter", "160")  # Height in cm
        else:
            # Select Gender: Male
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark"))).click()
            time.sleep(1)

            # Fill Male Inputs
            self.clear_and_enter_text(By.NAME, "cage", "25")  # Age
            self.clear_and_enter_text(By.NAME, "cweightkgs", "70")  # Weight in kg
            self.clear_and_enter_text(By.ID, "cheightmeter", "180")  # Height in cm

        # Pause before clicking Calculate
        time.sleep(1)

        # Click Calculate Button
        self.driver.find_element(By.NAME, "x").click()

        # Pause to allow results to load
        time.sleep(1)

        # Verify Results
        result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "font b"))).text

        if gender == "female":
            assert "Body Fat:" in result, "Unexpected result for female"
        else:
            assert "Body Fat:" in result, "Unexpected result for male"

        print(f"Body Fat Calculation Result for {gender}:", result)

        # Additional Test Cases (Optional)
        test_cases = [
            {"age": "20", "weight": "65", "height": "165"},
            {"age": "35", "weight": "75", "height": "175"},
            {"age": "50", "weight": "85", "height": "185"}
        ]

        for case in test_cases:
            time.sleep(1)  # Pause before entering new inputs
            self.clear_and_enter_text(By.NAME, "cage", case["age"])
            self.clear_and_enter_text(By.NAME, "cweightkgs", case["weight"])
            self.clear_and_enter_text(By.ID, "cheightmeter", case["height"])
            time.sleep(1)  # Pause before clicking Calculate
            self.driver.find_element(By.NAME, "x").click()
            time.sleep(1)  # Pause to allow results to load
            # Verify that results appear
            assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "font b"))), "Results not displayed"
