from selene import browser, have, be
from qa_guru_python_diploma.pages.web.base_page import open_main_page


def test_whats_new():
    # GIVEN
    open_main_page()

    browser.element('[data-test="menu_section_whatsnew"]').should(be.visible).click()
    browser.element('.nbl-segmentControlItem__caption:nth-child(1)').should(have.text('Что нового'))


def test_movies():
    # GIVEN
    open_main_page()

    browser.element('[data-test="menu_section_films"]').should(be.visible).click()
    browser.element('.headerBar__title').should(have.text('Фильмы смотреть онлайн'))


def test_serials():
    # GIVEN
    open_main_page()

    browser.element('[data-test="menu_section_menu_serials"]').should(be.visible).click()
    browser.element('.headerBar__title').should(have.text('Сериалы смотреть онлайн'))


def test_cartoons():
    # GIVEN
    open_main_page()

    browser.element('[data-test="menu_section_kids"]').should(be.visible).click()
    browser.element('.headerBar__title').should(have.text('Мультфильмы смотреть онлайн'))
