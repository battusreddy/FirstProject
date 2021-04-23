from selenium import webdriver
import pytest
import pytest_metadata
import pytest_html


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####pytest HTML REPORT
def pytest_configure(config):
    config._metadata['Proj Name']='Suresh Automation'
    config._metadata['tester']='SureshB'