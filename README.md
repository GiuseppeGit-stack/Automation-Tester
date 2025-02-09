# Selenium Automated Test for SauceDemo

## Description
This Selenium script automates the process of logging into the SauceDemo website, adding items to the cart, proceeding to checkout, and completing the purchase. The script runs using **Selenium WebDriver** and **Google Chrome**.

---

## Requirements
### Prerequisites
Before running the script, ensure you have the following installed:
- Python (>=3.x)
- Google Chrome (latest version)
- ChromeDriver (compatible with the installed Chrome version)
- Selenium Python package

### Install Dependencies
To install the necessary dependencies, run:
```bash
pip install selenium
```

---

## Script Breakdown

### 1. Set Up Selenium WebDriver
The script initializes a Chrome WebDriver instance with options to suppress DevTools logging.
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
```

### 2. Open SauceDemo Website
```python
driver.get("https://www.saucedemo.com/")
sleep(3)
```

### 3. Perform Login
The script locates and inputs login credentials:
```python
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)
```

### 4. Add Items to the Cart
The script selects and adds five items to the shopping cart.
```python
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in add_to_cart_btns[:5]:
    btns.click()
cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert "5" in cart_value.text
```

### 5. Navigate to Checkout
```python
cart_value_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_value_link.click()
sleep(5)
checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
checkout_button.click()
sleep(6)
```

### 6. Enter Checkout Information
The script enters the user's personal information:
```python
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys("Giuseppe")
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Di Perna")
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input").send_keys("65100")
```

### 7. Complete the Purchase
```python
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]").click()
sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/button").click()
sleep(5)
```

### 8. Close the Browser
```python
driver.quit()
```

---

## Running the Script
1. Ensure all dependencies are installed.
2. Save the script as `sauce_demo_test.py`.
3. Run the script:
```bash
python sauce_demo_test.py
```

---

## Debugging
If the script encounters errors:
- Ensure ChromeDriver is installed and matches your Chrome version.
- Check the SauceDemo site for any UI updates that might have changed element selectors.
- Run the script step-by-step to identify issues.

This script is useful for testing automation in web applications using **Selenium WebDriver**.

