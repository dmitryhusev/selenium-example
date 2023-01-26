

def test1(browser):
    browser.get('https://google.com')
    assert 1


def test2(browser):
    browser.get('https://google.com')
    assert 0