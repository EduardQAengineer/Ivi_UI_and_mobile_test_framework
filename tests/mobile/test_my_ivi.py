import allure

from qa_guru_python_diploma.pages.mobile import my_ivi


@allure.epic('My Ivi')
@allure.story("Movies")
class TestMyIvi:
    @allure.title("Serials sections should be shown")
    @allure.feature("Serials sections")
    @allure.label("microservice", "My Ivi")
    @allure.label("owner", "allure8")
    @allure.tag("regress", "mobile")
    @allure.severity('normal')
    def test_serials_sections_should_be_shown(self):
        # WHEN
        my_ivi.tap_on_my_ivi()

        # THEN
        my_ivi.serials_should_be_shown()

    @allure.title("Select movie in recommends")
    @allure.feature("Recommends section")
    @allure.label("microservice", "My Ivi")
    @allure.label("owner", "allure8")
    @allure.tag("regress", "mobile")
    @allure.severity('normal')
    def test_select_movie_in_recommends(self):
        # WHEN
        my_ivi.tap_on_recommend_movie()

        # THEN
        my_ivi.button_watch_should_be_shown()
