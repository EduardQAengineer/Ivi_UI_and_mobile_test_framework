from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


def confirm_cookie():
    with step('Confirm cookie'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Соглашаюсь"]')).click()


def tap_on_my_ivi():
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()


def tap_on_profile():
    with step('Tap on "Профиль"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).click()
