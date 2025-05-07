from selenium.webdriver.common.by import By

from tests.pageObjects.confirm_page import ConfirmPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    card_list = (By.XPATH, "//div[@class='card h-100']//h4/a")
    # card_text = (By.XPATH, ".//h4/a")
    add_card = (By.XPATH, "//div[@class='card-footer']/button")
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    chkout_page_button = (By.CSS_SELECTOR, "button[class*=btn-success]")

    def get_cards(self):
        return self.driver.find_elements(*ProductPage.card_list)

    # def get_card_text(self):
    #     return self.driver.find_element(*ProductPage.card_text)
    #
    def add_button(self):
        return self.driver.find_element(*ProductPage.add_card)

    def click_checkout_button(self):
        return self.driver.find_element(*ProductPage.checkout_button)

    def chkout_page_btn(self):
        self.driver.find_element(*ProductPage.chkout_page_button).click()

        confirm_page = ConfirmPage(self.driver)
        return confirm_page

