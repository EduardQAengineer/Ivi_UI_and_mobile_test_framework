import allure
import pytest

from qa_guru_python_diploma.pages.mobile import my_ivi
from tests.marks import microservice, layer, owner


@allure.title("Serials sections should be shown")
@allure.story("Serials")
@allure.feature("Serials sections")
@microservice("Serials")
@layer("Mobile")
@owner("allure8")
@pytest.mark.regress
@pytest.mark.mobile
def test_serials_sections_should_be_shown():
    # WHEN
    my_ivi.tap_on_my_ivi()

    # THEN
    my_ivi.serials_should_be_shown()


@allure.title("Select movie in recommends")
@allure.story("Recommended movies")
@allure.feature("Recommends section")
@microservice("Recommends")
@layer("Mobile")
@owner("allure8")
@pytest.mark.regress
@pytest.mark.mobile
def test_select_movie_in_recommends():
    # WHEN
    my_ivi.tap_on_recommend_movie()

    # THEN
    my_ivi.button_watch_should_be_shown()
