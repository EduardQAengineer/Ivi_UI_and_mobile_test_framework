from selene import browser, have, be
from allure import step


def open_main_page():
    with step('Открыть главную страницу'):
        browser.open('/')


def my_ivi_at_top_menu_should_be_visible():
    with step('Мой Иви - отображается в верхнем меню'):
        browser.element('#headerTop').should(have.text('Мой Иви'))


def click_on_movie_preview():
    with step('Нажать на превью'):
        browser.element('[data-content-id="16974"]').should(be.visible).click()


def movie_title_should_be_visible():
    with step('Заголовок фильма - отображается'):
        browser.element('[data-testid="watchTitle"]').should(have.text('Сериал Блеск смотреть онлайн'))


def click_on_promo():
    with step('нажать на промо'):
        browser.element('.teaserPlate.home__teaserPlate').should(be.visible).click()


def check_promo_title():
    with step('Проверить заголовок промо акции'):
        browser.element('.segmentedLanding__title.segmentedLanding__title_default').should(have.text('Подписка Иви'))


def check_promo_button():
    with step('Проверить кнопку промо акции'):
        browser.element('.nbl-button.nbl-button_textAlign_center.nbl-button_style_kioshi.nbl-button_hasBadge_0.segmentedLanding__nbl-button .nbl-button__primaryText').should(have.text('Попробовать 60 дней бесплатно'))
