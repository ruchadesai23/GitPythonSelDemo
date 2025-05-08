import pytest
from selenium.webdriver.support.select import Select

from test_Data.home_page_test_data import HomePageTestData
from tests.pageObjects.home_page import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, getdata):  # we need to define the fixture class here after self
        log = self.log_tests()
        home_page = HomePage(self.driver)

        log.info("First name is " + getdata["first_name"])
        home_page.add_name().send_keys(getdata["first_name"])  # this will get the value at 0th index

        log.info("Email is " + getdata["email"])
        home_page.add_email().send_keys(getdata["email"])

        log.info("password is " + str(getdata["password"]))
        home_page.enter_password().send_keys(getdata["password"])

        home_page.select_ice_checkbox().click()

        log.info("gender is " + getdata["gender"])
        self.select_option_by_text(home_page.select_gender(), getdata["gender"])

        home_page.click_submit().click()

        message = home_page.verify_success_message().text
        log.info("success message is " + message)
        assert "Success" in message

        self.driver.refresh()

    # we are defining fixture here because currently this fixture will only be used here.
    # so there is no use to put this fixture in conftest
    @pytest.fixture(
        params=HomePageTestData.get_exceltest_data("Testcase 2"))  # giving the testcase name which is needed
    def getdata(self, request):
        return request.param

# above this fixture will return all the parameters set in the dictionary in home_page_test_data file. we have imported
# in the test data package here.
    print("Hello! World.")
    print("changes by architect1 in develop branch")
    print("changes by architect2 - git stuff in develop branch")
