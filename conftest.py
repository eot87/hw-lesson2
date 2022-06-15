from selene.support.shared import browser
import pytest

@pytest.fixture(autouse=True)
def test_open_google():
    browser.open('https://google.com').driver.set_window_size(1380, 1000)
    print("Browser is open")