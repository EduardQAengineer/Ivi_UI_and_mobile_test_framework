import allure

from ivi_ui_and_mobile_test_framework.pages.web.base_page import open_main_page
from ivi_ui_and_mobile_test_framework.pages.web.search import click_on_search, type_movie_title, search_result_should_be_visible


@allure.epic('Search')
@allure.story('find_movie')
@allure.title('find_movie_by_title')
@allure.feature('Search')
@allure.label('microservice', 'Search')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_find_movie_by_title():
    # GIVEN
    title = 'Хроники риддика'
    open_main_page()

    # WHEN
    click_on_search()
    type_movie_title(title)

    # THEN
    search_result_should_be_visible()
