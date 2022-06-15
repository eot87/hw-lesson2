from selene.support.shared import browser
from selene import be, have

def test_search_element(test_open_google):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    print("query is done")
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
    print("link is found")

def test_failed_search_element(test_open_google):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should_not(have.text('User-oriented Web UI browser tests in Python'))
    print("link wasn't found")
