import time
import unittest
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProdus(unittest.TestCase):
    PRIMUL_PRODUS = (By.CSS_SELECTOR, '[class="card-phone-new position-relative d-flex flex-md-column"]')
    COLOR_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter color btn-link"]')
    STORAGE_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter btn-secondary"]')
    CONDITION_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter btn-condition relative btn-secondary"]')
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[class="searchBarInput form-control"]')
    SEARCH_CONFIRM = (By.CSS_SELECTOR, 'rect[width="34"]')
    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//span[contains(text(), "Da, sunt de acord")]')
    NUME_PRODUS = (By.XPATH, '//*[@class="phone-title"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://flip.ro/magazin/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

    def testProdusIphone(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('iPhone 15')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.PRIMUL_PRODUS).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.COLOR_SELECT).click()
        self.driver.implicitly_wait(3)
        actualResult = self.driver.find_element(*self.NUME_PRODUS)
        expectedMessage = 'iPhone 15, Black, 128 GB, Excelent'
        time.sleep(2)
        self.assertEqual(expectedMessage, actualResult.text, 'nu e ceea ce trebuie cautat')

    def testProdusSamsung(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('Samsung, Galaxy S23')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.PRIMUL_PRODUS).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.COLOR_SELECT).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.STORAGE_SELECT).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.CONDITION_SELECT).click()
        self.driver.implicitly_wait(3)
        actualResult = self.driver.find_element(*self.NUME_PRODUS)
        expectedMessage = 'Galaxy S23 5G Dual Sim'
        time.sleep(2)
        self.assertEqual(expectedMessage, actualResult.text, 'nu e ceea ce trebuie cautat')

    def testProdusHuawei(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('huawei, nova 10')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.PRIMUL_PRODUS).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.CONDITION_SELECT).click()
        self.driver.implicitly_wait(3)
        actualResult = self.driver.find_element(*self.NUME_PRODUS)
        expectedMessage = 'Nova 10 SE Dual Sim'
        time.sleep(2)
        self.assertEqual(expectedMessage, actualResult.text, 'nu e ceea ce trebuie cautat')

    def testProdusXiaomi(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('Xiaomi, Xiaomi 12T')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.PRIMUL_PRODUS).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.CONDITION_SELECT).click()
        self.driver.implicitly_wait(3)
        actualResult = self.driver.find_element(*self.NUME_PRODUS)
        expectedMessage = 'Xiaomi 12T 5G Dual Sim'
        time.sleep(2)
        self.assertEqual(expectedMessage, actualResult.text, 'nu e ceea ce trebuie cautat')


