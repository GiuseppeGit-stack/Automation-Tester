from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep


# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.get("http://automationpractice.com/index.php")

#driver.get("https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup")
sleep(3)

# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

print("testing add to cart")
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# Click three buttons to make the cart_value 3
for btns in add_to_cart_btns[:5]:
    btns.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert "5" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")

sleep(5)
cart_value_link = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
cart_value_link.click()
sleep(5)

checkout_button = driver.find_element(By.CLASS_NAME,"checkout_button")
checkout_button.click()
sleep(6)

checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input ").send_keys("Giuseppe")
sleep(6)
checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input ").send_keys("Di Perna")
sleep(6)
checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input").send_keys("65100")
#checkout_button = driver.find_element(By.ID,"lastname").send_keys("Di Perna")
sleep(6)
checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input")
checkout_button.click()
sleep(5)
checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]")
checkout_button.click()
sleep(5)
checkout_button = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/button")
checkout_button.click()
sleep(5)

driver.quit()






