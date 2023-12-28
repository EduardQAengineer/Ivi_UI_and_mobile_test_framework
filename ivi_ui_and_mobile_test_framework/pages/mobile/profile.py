from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def button_auth_should_be_shown():
    with step('Button "Войти или зарегистрироваться" is shown'):
        (browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Войти или зарегистрироваться"]'))
         .should(have.text('Войти или зарегистрироваться')))
