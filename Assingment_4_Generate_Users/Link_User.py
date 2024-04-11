from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to recursively check presence of link, images, and keywords
def check_website(driver):
    try:
        # Find all anchor elements on the page using XPath
        links = driver.find_elements(By.XPATH, "//a[@href]")
        
        # Check if there are any links present
        if links:
            # Extend presence time by 10 seconds
            time.sleep(10)

            # Click on the first link found
            links[0].click()
            time.sleep(2)  # Wait for the page to load after clicking
            
            return True
        
        return False
    except Exception as e:
        print("Error occurred while checking website:", e)
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

        # Recursively check presence of link, images, and keywords
        presence_time_extended = check_website(driver)

        # Output presence time on the terminal
        if presence_time_extended:
            print("Link found. Presence time extended by 10 seconds and clicked on the first link.")
        else:
            print("No link found.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver
        if driver:
            driver.quit()

# Test the script against a website with a link
print("Testing against a website with a link:")
main("http://localhost:3001/")

# Test the script against a website without a link
print("\nTesting against a website without a link:")
main("file:///Users/evelyn/Downloads/no_link_.html")
