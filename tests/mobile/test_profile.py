from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


def test_profile():
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Соглашаюсь"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).click()
    (browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Войти или зарегистрироваться"]'))
     .should(have.text('Войти или зарегистрироваться')))
