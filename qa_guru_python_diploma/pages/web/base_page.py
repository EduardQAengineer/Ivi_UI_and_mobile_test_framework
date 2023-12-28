from selene import browser
from selene import browser, have, be


def open_main_page():
    browser.open('/')


def my_ivi_at_top_menu_should_be_visible():
    browser.element('#headerTop').should(have.text('Мой Иви'))


def click_on_movie_preview():
    browser.element('[data-content-id="16974"]').should(be.visible).click()


def movie_title_should_be_visible():
    browser.element('[data-testid="watchTitle"]').should(have.text('Сериал Блеск смотреть онлайн'))


def click_on_promo():
    browser.element('.teaserPlate.home__teaserPlate').should(be.visible).click()


def check_promo_title():
    browser.element('.segmentedLanding__title.segmentedLanding__title_default').should(have.text('Подписка Иви'))


def check_promo_button():
    browser.element('.nbl-button.nbl-button_textAlign_center.nbl-button_style_kioshi.nbl-button_hasBadge_0.segmentedLanding__nbl-button .nbl-button__primaryText').should(have.text('Попробовать 60 дней бесплатно'))
