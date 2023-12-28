import allure

from ivi_ui_and_mobile_test_framework.pages.mobile import control_menu


@allure.title('Control buttons should be shown')
@allure.epic('Bottom menu')
@allure.story('Bottom menu')
@allure.feature('Control buttons in bottom menu')
@allure.label('microservice', 'Bottom menu')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_control_buttons_should_be_shown():
    # THEN
    control_menu.button_my_ivi_should_be_shown()
    control_menu.button_catalog_should_be_shown()
    control_menu.button_downloads_should_be_shown()
    control_menu.button_profile_should_be_shown()
