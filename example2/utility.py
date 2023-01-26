import allure
from allure_commons.types import AttachmentType


def make_attachment(browser):
    allure.attach(browser.get_screenshot_as_png(), 'screenshot', AttachmentType.PNG)
    allure.attach(browser.current_url, 'url', AttachmentType.TEXT)


def attach_video(name):
    allure.attach(f'https://your_server_ip/video/{name}.mp4', 'video', AttachmentType.URI_LIST)
