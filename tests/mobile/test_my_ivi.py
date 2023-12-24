from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_movie_sections_should_be_shown():
    # WHEN
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()

    # THEN
    with step('Check movie sections'):
        with step('Best shows on subscription - are shown'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Лучшие сериалы в подписке"]')).should(have.text('Лучшие сериалы в подписке'))

        with step('High-rated subscription serials - are shown'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Сериалы с высоким рейтингом по подписке"]')).should(have.text('Сериалы с высоким рейтингом по подписке'))
