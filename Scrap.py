import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up Chrome options to add a user-agent
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.178 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled") # Prevent bot detection
driver = webdriver.Chrome(options=chrome_options)

# Open Amazon
driver.get("https://www.amazon.com")
print("Opened Amazon. Please enter the search term in the search bar manually.")

# Wait until the search bar is present
try:
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    print("Search bar located.")
except TimeoutException:
    print("Error: Unable to locate the search bar.")
    driver.quit()
    exit()

# Wait for user to input search and hit enter
input("After entering the search term in the search bar, press Enter to continue...")

# Wait for search results to load
print("Waiting for search results...")
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]"))
    )
    print("Search results loaded.")
except TimeoutException:
    print("Error: Timed out waiting for search results.")
    driver.quit()
    exit()

# Open CSV file to store the data
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating", "URL"])  # Write headers

    while True:
        # Extract product details on the current page
        try:
            print("Extracting data from the current page...")

            products = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")
            prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-price-whole')]")
            ratings = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-icon-alt')]")
            links = driver.find_elements(By.XPATH, "//a[contains(@class, 'a-link-normal s-no-outline')]")

            for i in range(len(products)):
                try:
                    name = products[i].text.strip()
                except Exception:
                    name = "Name not available"

                try:
                    price = prices[i].text.strip() if i < len(prices) else "Price not available"
                except Exception:
                    price = "Price not available"

                try:
                    rating = ratings[i].text.strip() if i < len(ratings) else "Rating not available"
                except Exception:
                    rating = "Rating not available"

                try:
                    url = "https://www.amazon.com" + links[i].get_attribute('href')
                except Exception:
                    url = "URL not available"

                writer.writerow([name, price, rating, url])
                print(f"Extracted: {name} | {price} | {rating} | {url}")

        except Exception as e:
            print(f"Error extracting product data: {e}")

        # Check for Next Page
        try:
            next_page_button = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Next page')]")
            print("Navigating to the next page...")
            driver.execute_script("arguments[0].click();", next_page_button)
            time.sleep(3)
        except NoSuchElementException:
            print("No more pages available. Scraping finished.")
            break

# Close the browser
print("Data scraping complete. Saved to products.csv")
driver.quit()
