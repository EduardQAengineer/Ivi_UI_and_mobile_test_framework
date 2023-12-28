import allure
from appium.webdriver.common.appiumby import AppiumBy

from ivi_ui_and_mobile_test_framework.pages.mobile import my_ivi
from selene import browser, have


@allure.epic('My Ivi')
@allure.story('Movies')
class TestMyIvi:
    @allure.title('Serials sections should be shown')
    @allure.feature('Serials sections')
    @allure.label('microservice', 'My Ivi')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'mobile')
    @allure.severity('normal')
    def test_serials_sections_should_be_shown(self):
        # WHEN
        my_ivi.tap_on_my_ivi()

        # THEN
        my_ivi.serials_should_be_shown()

    @allure.title('Select movie in recommends')
    @allure.feature('Recommends section')
    @allure.label('microservice', 'My Ivi')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'mobile')
    @allure.severity('normal')
    def test_select_movie_in_recommends(self):
        # WHEN
        my_ivi.tap_on_recommend_movie()

        # THEN
        my_ivi.button_watch_should_be_shown()

    def test_profile(self):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).click()
        (browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Войти или зарегистрироваться"]'))
         .should(have.text('Войти или зарегистрироваться')))
