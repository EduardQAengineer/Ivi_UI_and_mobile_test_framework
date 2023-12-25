from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_control_buttons_should_be_shown():
    # THEN
    with step('Button "Мой ivi" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).should(have.text('Мой ivi'))

    with step('Button "Каталог" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Каталог"]')).should(have.text('Каталог'))

    with step('Button "Загрузки" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Загрузки"]')).should(have.text('Загрузки'))

    with step('Button "Профиль" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).should(have.text('Профиль'))
