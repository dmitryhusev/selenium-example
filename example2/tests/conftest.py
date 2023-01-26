import pytest
from selenium import webdriver

from example2.utility import make_attachment, attach_video
from example2.browser_capability_handler import BrowserCapabilitiesHandler
from example2.test_state_handler import TestStateHandler


HOW_MANY_TIMES_TO_RERUN = 1

capabilities = BrowserCapabilitiesHandler()
test_state = TestStateHandler()


def add_video_on_last_test_rerun(name):
    if test_state.failure_count == HOW_MANY_TIMES_TO_RERUN:
        capabilities.enableVideo = True
    elif test_state.failure_count == HOW_MANY_TIMES_TO_RERUN + 1:
        attach_video(name)
        test_state.set_to_default_state()
        capabilities.set_to_default_state()


def pytest_exception_interact(node):
    test_state.failure_count += 1

    browser = node.funcargs.get('browser')
    if browser:
        make_attachment(browser)
        add_video_on_last_test_rerun(browser.session_id)


@pytest.fixture
def browser():
    # To record the video you definitely should use corresponding selenoid tools: selenoid + selenoid video recorder
    # They have all needed info on their official site
    # Instead of Chrome Remote browser should be used, like that:
    # driver = webdriver.Remote(f'{your_selenoid_ip}/wd/hub/', capabilities.get_capabilities())
    # so we update video capability here, add_video_on_last_test_rerun() function: capabilities.enableVideo = True
    # In the allure report you will see that video attachment is present only for a failed test, meaning that
    # on the first try there is no any video attachment (see screens in the README.md of this module)
    br = webdriver.Chrome()
    br.maximize_window()
    yield br
    br.quit()
