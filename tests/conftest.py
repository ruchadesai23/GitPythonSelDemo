from selenium import webdriver
import pytest

driver = None  # step for declaring global driver


# declaring and intialised a run time variable for selecting browser in runtime
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):  # this instance is necessary for connecting the driver to the class instance
    # to retrieve the commandline key value do below
    global driver

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":  # invocation chrome
        driver = webdriver.Chrome()
    elif browser_name == "firefox":  # invocation firefox
        driver = webdriver.Firefox()
    elif browser_name == "IE":  # invocation edge
        driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver  # we cannot use return driver, because return does not work when we use yield
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# the above screenshot mechanism can be simply copy pasted in conftest file so it can be available in all the tests.
# we will need to declare a global driver so the driver in the screenshot method is accessible
