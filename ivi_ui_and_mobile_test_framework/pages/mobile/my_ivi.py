from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def serials_should_be_shown():
    with step('Serials - are shown'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text, "Сериалы")]')).should(have.text('Сериалы'))


def tap_on_recommend_movie():
    with step('Tap on recommend movie'):
        browser.element((AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="ru.ivi.client:id/poster"])')).click()


def button_watch_should_be_shown():
    with step('Button "Смотреть" is shown'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Смотреть"]')).should(have.text('Смотреть'))
