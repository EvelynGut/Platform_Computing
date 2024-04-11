from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to check presence of keyword and extend presence time if found
def check_keyword_presence(driver):
    try:
        # Check if the keyword is present in the content
        keyword_present = "coding" in driver.page_source
        
        if keyword_present:
            # Extend presence time by 10 seconds
            time.sleep(10)
        
        return keyword_present
    except Exception as e:
        print("Error occurred while checking keyword presence:", e)
        return False

# Main function
def main(url):
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome()  # You can change this to your preferred WebDriver

        # Navigate to the URL
        driver.get(url)

        # Wait for the content to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Check presence of keyword and extend presence time if found
        keyword_present = check_keyword_presence(driver)

        # Output presence time on the terminal
        if keyword_present:
            print("Keyword found. Presence time extended by 10 seconds.")
        else:
            print("Keyword not found.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver
        driver.quit()

# Test the script against a website with the keyword
print("Testing against a website with the keyword:")
main("http://localhost:3001/")

# Test the script against a website without the keyword
print("\nTesting against a website without the keyword:")
main("https://www.pinterest.com/gutierreze01042/")
