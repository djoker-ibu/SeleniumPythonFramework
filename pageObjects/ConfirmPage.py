from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    checkOutbtn = (By.CSS_SELECTOR, "button[class*='btn-success']")
    # Checkout button in shop page
    locationKey = (By.CSS_SELECTOR, "#country")
    # Location dynamic dropbox
    locationText = (By.LINK_TEXT, "India")
    # Test in the dropbox
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # Checkbox in the same page for TnC
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    # Purchase button in the same page
    success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def CheckOut(self):
        return self.driver.find_element(*ConfirmPage.checkOutbtn).click()

    def location(self):
        self.driver.find_element(*ConfirmPage.locationKey).send_keys("Ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(*ConfirmPage.locationText).click()
        return self.driver.find_element(*ConfirmPage.checkbox).click()

    def purchaseBTN(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton).click()

    def purchaseSuccess(self):
        return self.driver.find_element(*ConfirmPage.success).text
        # assert "Success!" in success


