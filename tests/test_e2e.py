from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "BlackBerry":
                checkOutPage.getCardFooter()[i].click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        confirmpage = checkOutPage.checkOutItems()
        log.info("Entering country name and Ind")
        confirmpage.CheckOut()
        confirmpage.location()
        confirmpage.purchaseBTN()
        textMatch = confirmpage.purchaseSuccess()
        log.info("Text received from application is "+textMatch)
        assert "Success!" in textMatch  # Checking partial text instead of whole text
