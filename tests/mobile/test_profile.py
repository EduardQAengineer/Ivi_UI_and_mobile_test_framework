import allure

from ivi_ui_and_mobile_test_framework.pages.mobile import base_page, profile


@allure.epic('Profile')
@allure.story('Open profile')
@allure.title('Open profile')
@allure.feature('Profile')
@allure.label('microservice', 'Profile')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'mobile', 'critical')
@allure.severity('critical')
def test_open_profile():
    # WHEN
    base_page.confirm_cookie()
    base_page.tap_on_profile()

    # THEN
    profile.button_auth_should_be_shown()
