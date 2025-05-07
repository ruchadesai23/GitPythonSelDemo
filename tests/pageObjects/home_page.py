from selenium.webdriver.common.by import By
from tests.pageObjects.product_page import ProductPage


class HomePage:

    def __init__(self, driver):  # create the __init__ constructor so the class will treat it as its own constructor
        self.driver = driver

    # declare the shop locator
    shop = (By.XPATH, '//a[@href="/angularpractice/shop"]')  # setting a class variable
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    icecream_chkbox = (By.ID, "exampleCheck1")
    gender_drpdwn = (By.ID, "exampleFormControlSelect1")
    sbmit_btn = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def add_name(self):
        return self.driver.find_element(*HomePage.name)

    def add_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def select_ice_checkbox(self):
        return self.driver.find_element(*HomePage.icecream_chkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender_drpdwn)

    def click_submit(self):
        return self.driver.find_element(*HomePage.sbmit_btn)

    def verify_success_message(self):
        return self.driver.find_element(*HomePage.message)

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()  # calling the variable in the method
        # above we are doin the clck function in the POM.since we know it will take us to the elements of the next page.
        # we can call the class of the next page here

        prod_page = ProductPage(self.driver)  # create the object of the next page
        return prod_page  # return the object

    # above because shop is a class variable we need to add class.variable
    # above we need to add a star before homepage so it will treat the variable as a tuple and  deserialize the tuple
