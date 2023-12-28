from selene import browser, have, be
from allure import step


def click_on_search():
    with step('Нажать на кнопку поиска'):
        browser.element('[data-test="header_search"]').should(be.visible).click()


def type_movie_title(title):
    with step('Ввести название фильма'):
        browser.element('input[data-test="search_input"]').type(title).press_enter()


def search_result_should_be_visible():
    with step('Результаты поиска отображаются'):
        browser.element('.searchBlock.searchBlock_result').should(have.text('Также смотрят'))
