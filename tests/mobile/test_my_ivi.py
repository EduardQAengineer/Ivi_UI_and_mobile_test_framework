from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_serials_sections_should_be_shown():
    # WHEN
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()

    # THEN
    with step('Serials - are shown'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text, "Сериалы")]')).should(have.text('Сериалы'))


def test_select_movie_in_recommends():
    # WHEN
    with step('Tap on recommend movie'):
        browser.element((AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="ru.ivi.client:id/poster"])[2]')).click()

    # THEN
    with step('Button "Смотреть" is shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Смотреть"]')).should(have.text('Смотреть'))
