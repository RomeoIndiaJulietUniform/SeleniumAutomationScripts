import subprocess

try:
    import selenium
except ImportError:
    subprocess.check_call(["pip", "install", "selenium"])

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_and_search(email, password, search_query, chrome_driver_path):
    serv_obj = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://www.linkedin.com/")
    time.sleep(3)

    email_field = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")

    if email_field and password_field:
        email_field.send_keys(email)
        password_field.send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button").click()
        time.sleep(4)
        print("Logged in successfully!")
    else:
        print("Already logged in or login fields not found.")

    search_box = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search')]")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(8)

    driver.quit()

if __name__ == "__main__":
    email = input("Enter your LinkedIn email: ")
    password = input("Enter your LinkedIn password: ")
    search_query = input("Enter your search query: ")
    chrome_driver_path = input("Enter the path to ChromeDriver: ")
    login_and_search(email, password, search_query, chrome_driver_path)
