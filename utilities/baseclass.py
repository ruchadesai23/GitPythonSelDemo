import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# here we are updating the setup fixture and then will inherit the baseclass
# in all the tests instead of using the pytest fixture again and again
# this approach helps us to have clear test
@pytest.mark.usefixtures("setup")
class BaseClass:
    # pass  # pass is a keyword used to say there is no operation being performed here

    def log_tests(self):
        logger_name = self.__class__.__name__  # Gets the actual test class name
        logger = logging.getLogger(logger_name)

        if not logger.handlers: # Prevent adding duplicate handlers i.e if there multiple scenarios in a
            # single test the logger will not be handled multiple times
            filehandler = logging.FileHandler("logfile.log")
            formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)  # pass the filehandler object - filehandler means file name
            logger.setLevel(logging.DEBUG)
        return logger # Return logger so it can be used

    def verifying_link_presence(self, text):  # enter expected argument after self
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        # adding the expected argument so we can add the actual text in the testcase

    def select_option_by_text(self, locator, text):  # we add the expected parameters after self
        sel = Select(locator)  # here expected is locator which will change with testcases
        sel.select_by_visible_text(text)  # here text will change by testcase
