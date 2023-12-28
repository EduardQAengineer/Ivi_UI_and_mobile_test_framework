from selene import browser, have, be


def click_on_whats_new():
    browser.element('[data-test="menu_section_whatsnew"]').should(be.visible).click()


def check_whats_new_title():
    browser.element('.nbl-segmentControlItem__caption:nth-child(1)').should(have.text('Что нового'))


def click_on_movies():
    browser.element('[data-test="menu_section_films"]').should(be.visible).click()


def check_movies_title():
    browser.element('.headerBar__title').should(have.text('Фильмы смотреть онлайн'))


def click_on_serials():
    browser.element('[data-test="menu_section_menu_serials"]').should(be.visible).click()


def check_serials_title():
    browser.element('.headerBar__title').should(have.text('Сериалы смотреть онлайн'))


def click_on_cartoons():
    browser.element('[data-test="menu_section_kids"]').should(be.visible).click()


def check_cartoons_title():
    browser.element('.headerBar__title').should(have.text('Мультфильмы смотреть онлайн'))
