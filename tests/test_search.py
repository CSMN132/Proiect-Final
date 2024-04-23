import time
import unittest
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Search_Bar(unittest.TestCase):
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[class="searchBarInput form-control"]')
    SEARCH_CONFIRM = (By.CSS_SELECTOR, 'rect[width="34"]')
    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//span[contains(text(), "Da, sunt de acord")]')
    PRODUCT_ITEM = (By.XPATH, '//div[@data-cy="phone-title"]')


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://flip.ro/magazin/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

    def test_search_apple(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('iphone 15')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(1)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM)
        expectedMessage = 'Apple, iPhone 15'
        time.sleep(1)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')

    def test_search_samsung(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('Samsung, Galaxy S23')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(1)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM)
        expectedMessage = 'Samsung, Galaxy S23'
        time.sleep(1)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')

    def test_search_huawei(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('huawei, P30')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(1)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM)
        expectedMessage = "Huawei, P30"
        time.sleep(1)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')

    def test_search_xiaomi(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('xiaomi, 12 pro')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(1)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM)
        expectedMessage = 'Xiaomi, Xiaomi 12T'
        time.sleep(1)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')

    def test_search_ipad(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('Apple, iPad Air 5')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(1)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM)
        expectedMessage = 'Apple, iPad Air 5'
        time.sleep(1)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')