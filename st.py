from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import unittest
import random
import time

login_data = [
    ["650523example_email@email.com", "password"],
    ["952619example_email@email.com", "password"],
    ["449423example_2@email.com", "anotherpassword"],
    ["662782example_5@email.com", "anotherpassword"],
    ["660661x@y.com", "thirdpassword"],
    ["355761x@y.com", "thirdpassword"]
]

search_data = [
    "dress",
    "t-shirts",
    "blouses",
    "woman",
    "summer"
]

title_xpath = "/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div/div/span"
menu_data = [
    ["Women", "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a"],
    ["Dresses", "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a"],
    ["T-shirts", "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a"]
]

class Selenium_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        with open('data.csv') as csvfile:
            csvreader = reader(csvfile, delimiter=',')
            for row in csvreader:
                assert self.driver.find_element(*locator["sign_in_link"]).is_displayed()
                self.driver.find_element(*locator["sign_in_link"]).click()
                self.driver.find_element(*locator["email_field"]).send_keys(str(random.randint(0,1000000))+row[0])
                self.driver.find_element(*locator["create_account_button"]).click()
                assert self.driver.title == "Login - My Store"
                self.driver.find_element(*locator["gender_radiobutton"]).click()
                self.driver.find_element(*locator["firstname"]).send_keys(row[1])
                self.driver.find_element(*locator["lastname"]).send_keys(row[2])
                self.driver.find_element(*locator["password"]).send_keys(row[3])
                select = Select(self.driver.find_element(*locator["days_dropdown"]))
                select.select_by_value(row[4])
                select = Select(self.driver.find_element(*locator["months_dropdown"]))
                select.select_by_value(row[5])
                select = Select(self.driver.find_element(*locator["years_dropdown"]))
                select.select_by_value(row[6])
                self.driver.find_element(*locator["newsletter_checkbox"]).click()
                self.driver.find_element(*locator["optin_checkbox"]).click()
                self.driver.find_element(*locator["address"]).send_keys(row[7])
                self.driver.find_element(*locator["city"]).send_keys(row[8])
                select = Select(self.driver.find_element(*locator["state_dropdown"]))
                select.select_by_visible_text(row[9])
                self.driver.find_element(*locator["postcode"]).send_keys(row[10])
                self.driver.find_element(*locator["mobile"]).send_keys(row[11])
                self.driver.find_element(*locator["register_button"]).click()
                assert self.driver.title == "My account - My Store"
                self.driver.find_element(*locator["logout_button"]).click()

    def test_correct_login(self):
        for item in login_data:
            assert self.driver.find_element(*locator["sign_in_link"]).is_displayed()
            self.driver.find_element(*locator["sign_in_link"]).click()
            assert self.driver.title == "Login - My Store"
            self.driver.find_element(*locator["email"]).send_keys(item[0])
            self.driver.find_element(*locator["password"]).send_keys(item[1])
            self.driver.find_element(*locator["login_button"]).click()
            self.driver.find_element(*locator["logout_button"]).click()

    def test_incorrect_login(self):
        for _ in range(3):
            random_email  = str(random.randint(0, 1000000))+"@email.com"
            random_passwd = str(random.randint(100000, 1000000000))
            assert self.driver.find_element(
                *locator["sign_in_link"]).is_displayed()
            self.driver.find_element(*locator["sign_in_link"]).click()
            assert self.driver.title == "Login - My Store"
            self.driver.find_element(*locator["email"]).send_keys(random_email)
            self.driver.find_element(*locator["password"]).send_keys(random_passwd)
            self.driver.find_element(*locator["login_button"]).click()
            self.driver.find_element(*locator["login_error_message"]).text == "Authentication failed."

    def test_search(self):
        for item in search_data:
            self.driver.find_element(*locator["search"]).clear()
            self.driver.find_element(*locator["search"]).send_keys(item)
            self.driver.find_element(*locator["search_botton"]).click()
            assert self.driver.title == "Search - My Store"

    def test_menu(self):
        for item in menu_data:
            self.driver.find_element_by_xpath(item[1]).click()
            assert self.driver.title == item[0] + " - My Store"
            assert self.driver.find_element_by_xpath(title_xpath).text == item[0]
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
