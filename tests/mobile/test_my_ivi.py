import allure

from ivi_ui_and_mobile_test_framework.pages.mobile import my_ivi, base_page


@allure.epic('My Ivi')
@allure.story('Movies')
@allure.title('Serials sections should be shown')
@allure.feature('Serials sections')
@allure.label('microservice', 'My Ivi')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'mobile')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_serials_sections_should_be_shown():
    # WHEN
    base_page.confirm_cookie()
    base_page.tap_on_my_ivi()

    # THEN
    my_ivi.serials_should_be_shown()
