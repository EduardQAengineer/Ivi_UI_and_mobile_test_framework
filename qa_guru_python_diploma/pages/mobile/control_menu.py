from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def button_my_ivi_should_be_shown():
    with step('Button "Мой ivi" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).should(have.text('Мой ivi'))


def button_catalog_should_be_shown():
    with step('Button "Каталог" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Каталог"]')).should(have.text('Каталог'))


def button_downloads_should_be_shown():
    with step('Button "Загрузки" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Загрузки"]')).should(have.text('Загрузки'))


def button_profile_should_be_shown():
    with step('Button "Профиль" are shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).should(have.text('Профиль'))
