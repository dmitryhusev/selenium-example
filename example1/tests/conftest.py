import pytest
from selenium import webdriver

from example1.utility import make_attachment


def pytest_exception_interact(node):
    browser = node.funcargs.get('browser')
    if browser:
        make_attachment(browser)


@pytest.fixture
def browser():
    br = webdriver.Firefox()
    br.maximize_window()
    yield br
    br.quit()
