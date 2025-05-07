from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    ctry_drpdown_list = (By.XPATH, "//input[@id='country']")
    cntry_option = (By.LINK_TEXT, "India")
    trm_chkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    prchse_btn = (By.CSS_SELECTOR, "input[type='submit']")
    sccess_msg = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def country_dropdown(self):
        return self.driver.find_element(*self.ctry_drpdown_list)

    def country_option(self):
        return self.driver.find_element(*self.cntry_option)

    def select_term_checkbox(self):
        return self.driver.find_element(*self.trm_chkbox)

    def purchase_button(self):
        return self.driver.find_element(*self.prchse_btn)

    def success_message(self):
        return self.driver.find_element(*self.sccess_msg)





