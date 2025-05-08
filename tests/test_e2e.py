import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pageObjects.confirm_page import ConfirmPage
from tests.pageObjects.home_page import HomePage
from tests.pageObjects.product_page import ProductPage
from utilities.baseclass import BaseClass


class TestOne(BaseClass):
    # above, the baseclass brings the knowledge of the fixture, so we don't need to add it in every test
    def test_e2e(self):
        log = self.log_tests() # because we are getting the base class in the class, we just need to call it using self
        homepage = HomePage(self.driver)
        # click on the Shop link is not required here since this action is being performed in the POM
        # homepage.shop_items().click()
        prod_page = homepage.shop_items()  # this is returned in home page so we can catch this object here
        # prod_page = ProductPage(self.driver) # this is not required coz we called this class in home page pom
        # we will search all the products and click on add
        log.info("Getting all card titles") # using info log to get the title names
        prod_list = prod_page.get_cards()

        # confirm_page = ConfirmPage(self.driver)
        # - we dont need this since confirm page object is directly called in the product page class

        for product in prod_list:

            prod_name = product.text
            if prod_name == "Blackberry":
                log.info(prod_name)
                prod_page.add_button().click()

        # click on checkout
        prod_page.click_checkout_button().click()

        # click on checkout in cart screen
        confirm_page = prod_page.chkout_page_btn()  # calling the confirm page object in the

        log.info("entering country text - 'Ind'")
        # enter Ind in the textbox
        confirm_page.country_dropdown().send_keys("Ind")

        # waiting for the dropdown to be present
        self.verifying_link_presence(
            "India")  # calling the wait method from baseclass mentioning the expected text here

        # select India from the autosuggestion box
        confirm_page.country_option().click()

        # select on terms checkbox
        confirm_page.select_term_checkbox().click()

        # click on purchase button
        confirm_page.purchase_button().click()

        # verifying success message
        success_message = confirm_page.success_message().text
        log.info("text received from application is " + success_message)
        assert "Success! Thank you!" in success_message

        print("Hello! World.")
        print("Hello! World. by gitstuff")
        print("changes by architect1 in develop branch")
        print("changes by architect2 - git stuff in develop branch")
