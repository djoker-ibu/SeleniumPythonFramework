import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # homepage.getName().send_keys(getData[0])
        log.info("First Name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        # homepage.getEmail().send_keys(getData[1])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckbox().click()
        # self.selectOptionByText(homepage.getGender(), getData[2])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert "Success" in alertText
        self.driver.refresh()

    # @pytest.fixture(params=[("Ibu", "djoker@mail.com", "Male"), ("Boo", "djoking@mail.com", "Female")])
    # params also supports dictionary
    @pytest.fixture(params=HomePageData.getTestData("data1"))
    def getData(self, request):
        return request.param
