import allure

from ivi_ui_and_mobile_test_framework.pages.web.base_page import open_main_page, my_ivi_at_top_menu_should_be_visible, \
    click_on_movie_preview, movie_title_should_be_visible, click_on_promo, check_promo_title, check_promo_button


@allure.epic('Base page')
class TestBasePage:
    @allure.story('Open base page')
    @allure.title('Base page should be shown')
    @allure.feature('Base page')
    @allure.label('microservice', 'Base page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    def test_open_base_page(self):
        # GIVEN
        open_main_page()

        # THEN
        my_ivi_at_top_menu_should_be_visible()

    @allure.story('Open movie page')
    @allure.title('Mobie title should be shown')
    @allure.feature('Movie page')
    @allure.label('microservice', 'Movie page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    def test_open_movie_page(self):
        # GIVEN
        open_main_page()

        # WHEN
        click_on_movie_preview()

        # THEN
        movie_title_should_be_visible()

    @allure.story('Open promo page')
    @allure.title('Promo page should be shown')
    @allure.feature('Promo page')
    @allure.label('microservice', 'Promo page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    def test_open_promo_page(self):
        # GIVEN
        open_main_page()

        # WHEN
        click_on_promo()

        # THEN
        check_promo_title()
        check_promo_button()
