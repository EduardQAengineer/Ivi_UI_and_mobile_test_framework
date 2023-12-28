from selene import browser, have, be


def click_on_search():
    browser.element('[data-test="header_search"]').should(be.visible).click()


def type_movie_title(title):
    browser.element('input[data-test="search_input"]').type(title).press_enter()


def search_result_should_be_visible():
    browser.element('.searchBlock.searchBlock_result').should(have.text('Также смотрят'))
