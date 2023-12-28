from selene import browser, have, be
from allure import step


class TopMenu:
    title = '.headerBar__title'

    @staticmethod
    def click_on_whats_new():
        with step('Нажать на кнопку "Что нового"'):
            browser.element('[data-test="menu_section_whatsnew"]').should(be.visible).click()

    @staticmethod
    def check_whats_new_title():
        with step('Проверить заголовок "Что нового"'):
            browser.element('.nbl-segmentControlItem__caption:nth-child(1)').should(have.text('Что нового'))

    @staticmethod
    def click_on_movies():
        with step('нажать на кнопку "Фильмы"'):
            browser.element('[data-test="menu_section_films"]').should(be.visible).click()

    def check_movies_title(self):
        with step('Проверить заголовок "Фильмы"'):
            browser.element(self.title).should(have.text('Фильмы смотреть онлайн'))

    @staticmethod
    def click_on_serials():
        with step('Нажать на кнопку "Сериалы"'):
            browser.element('[data-test="menu_section_menu_serials"]').should(be.visible).click()

    def check_serials_title(self):
        with step('Проверить заголовок "Сериалы"'):
            browser.element(self.title).should(have.text('Сериалы смотреть онлайн'))

    @staticmethod
    def click_on_cartoons():
        with step('нажать на кнопку "Мультфильмы"'):
            browser.element('[data-test="menu_section_kids"]').should(be.visible).click()

    def check_cartoons_title(self):
        with step('Проверить заголовок "Мультфильмы"'):
            browser.element(self.title).should(have.text('Мультфильмы смотреть онлайн'))
