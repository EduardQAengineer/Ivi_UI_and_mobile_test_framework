import allure

from ivi_ui_and_mobile_test_framework.pages.web.base_page import open_main_page
from ivi_ui_and_mobile_test_framework.pages.web.top_menu import TopMenu

top_menu = TopMenu()


@allure.epic('Top menu')
class TestTopMenu:
    @allure.story('Open what\'s new page')
    @allure.title('What\'s new page should be shown')
    @allure.feature('What\'s new page')
    @allure.label('microservice', 'what\'s new page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    @allure.label('layer', 'web')
    def test_whats_new(self):
        # GIVEN
        open_main_page()

        # WHEN
        top_menu.click_on_whats_new()

        # THEN
        top_menu.check_whats_new_title()

    @allure.story('Open movies page')
    @allure.title('Movies page should be shown')
    @allure.feature('Movies page')
    @allure.label('microservice', 'Movies page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    @allure.label('layer', 'web')
    def test_movies(self):
        # GIVEN
        open_main_page()

        # WHEN
        top_menu.click_on_movies()

        # THEN
        top_menu.check_movies_title()

    @allure.story('Open serials page')
    @allure.title('Serials page should be shown')
    @allure.feature('Serials page')
    @allure.label('microservice', 'Serials page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    @allure.label('layer', 'web')
    def test_serials(self):
        # GIVEN
        open_main_page()

        # WHEN
        top_menu.click_on_serials()

        # THEN
        top_menu.check_serials_title()

    @allure.story('Open cartoons page')
    @allure.title('Cartoons page should be shown')
    @allure.feature('Cartoons page')
    @allure.label('microservice', 'Cartoons page')
    @allure.label('owner', 'allure8')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    @allure.label('layer', 'web')
    def test_cartoons(self):
        # GIVEN
        open_main_page()

        # WHEN
        top_menu.click_on_cartoons()

        # THEN
        top_menu.check_cartoons_title()
