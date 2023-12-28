import allure
import pytest

from qa_guru_python_diploma.pages.mobile import control_menu
from tests.marks import microservice, layer, owner


@allure.title("Control buttons should be shown")
@allure.story("Bottom menu")
@allure.feature("Control buttons in bottom menu")
@microservice("Bottom menu")
@layer("Mobile")
@owner("allure8")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.mobile
@pytest.mark.critical
def test_control_buttons_should_be_shown():
    # THEN
    control_menu.button_my_ivi_should_be_shown()
    control_menu.button_catalog_should_be_shown()
    control_menu.button_downloads_should_be_shown()
    control_menu.button_profile_should_be_shown()
