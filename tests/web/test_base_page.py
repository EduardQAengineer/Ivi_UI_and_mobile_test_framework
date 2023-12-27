from selene import browser, have, be
from qa_guru_python_diploma.pages.web.base_page import open_main_page


def test_open_base_page():
    # GIVEN
    open_main_page()

    browser.element('#headerTop').should(have.text('Мой Иви'))


def test_open_movie():
    # GIVEN
    open_main_page()

    browser.element('[data-content-id="16974"]').should(be.visible).click()
    browser.element('[data-testid="watchTitle"]').should(have.text('Сериал Блеск смотреть онлайн'))


def test_open_promo():
    # GIVEN
    open_main_page()

    browser.element('.teaserPlate.home__teaserPlate').should(be.visible).click()
    browser.element('.segmentedLanding__title.segmentedLanding__title_default').should(have.text('Подписка Иви'))
    browser.element('.nbl-button.nbl-button_textAlign_center.nbl-button_style_kioshi.nbl-button_hasBadge_0.segmentedLanding__nbl-button .nbl-button__primaryText').should(have.text('Попробовать 60 дней бесплатно'))
