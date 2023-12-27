from selene import browser, have, be


def test_find_movie_by_title():
    browser.open('/')
    browser.element('[data-test="header_search"]').should(be.visible).click()
    browser.element('input[data-test="search_input"]').type('Хроники риддика').press_enter()
    browser.element('.searchBlock.searchBlock_result').should(have.text('Также смотрят'))

