from selene import browser, have, be
from qa_guru_python_diploma.pages.web.base_page import open_main_page


def test_find_movie_by_title():
    # GIVEN
    open_main_page()

    # WHEN
    browser.element('[data-test="header_search"]').should(be.visible).click()
    browser.element('input[data-test="search_input"]').type('Хроники риддика').press_enter()

    # THEN
    browser.element('.searchBlock.searchBlock_result').should(have.text('Также смотрят'))
