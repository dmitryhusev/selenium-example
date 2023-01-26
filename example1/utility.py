import allure
from allure_commons.types import AttachmentType


def make_attachment(browser):
    allure.attach(browser.get_screenshot_as_png(), 'screenshot', AttachmentType.PNG)
    allure.attach(browser.current_url, 'url', AttachmentType.TEXT)
