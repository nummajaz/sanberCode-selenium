import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginKasir1(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path='C:/Users/lenov/Documents/belajar/sanbercode_QA/sanber_Selenium/sanberCode_Selenium/chromedriver.exe')
        self.browser = webdriver.Chrome(service=service, options=options)

    def testFailedLogin(self):
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com/login")
        driver.find_element(By.ID, "email").send_keys("xxxx")
        driver.find_element(By.ID, "password").send_keys("xxxx")
        driver.find_element(By.CLASS_NAME, "chakra-button css-1n8i4of").click()

    def tearDown(self):
        self.browser.close()
    
    if __name__ == "__main__":
        unittest.main() 
