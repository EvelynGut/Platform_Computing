from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Main function
def main(url):
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome()  # You can change this to your preferred WebDriver

        # Navigate to the URL
        driver.get(url)

        # Wait for the content to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Check presence of images using JavaScript
        num_images = driver.execute_script("return document.getElementsByTagName('img').length")

        # Output presence time on the terminal
        if num_images > 0:
            print(f"Images found: {num_images}. Presence time extended by {num_images * 10} seconds.")
        else:
            print("No images found.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver
        if driver:
            driver.quit()

# Test the script against a website with images
print("Testing against a website with images:")
main("https://www.pinterest.com/gutierreze01042/")

# Test the script against a website without images
print("\nTesting against a website without images:")
main("https://chat.openai.com/")
