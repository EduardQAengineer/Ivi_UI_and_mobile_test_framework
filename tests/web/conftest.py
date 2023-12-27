import pytest
import os

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_python_diploma.utils import allure_attach


DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser-version',
        help='Версия браузера в которой будут запущены тесты',
        default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser-version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    remote_browser_url = os.getenv('REMOTE_BROWSER_URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{remote_browser_url}",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://ivi.ru"
    browser.config.window_height = 1921
    browser.config.window_width = 1801

    yield browser

    allure_attach.screenshot(browser)
    allure_attach.logs(browser)
    allure_attach.html(browser)
    allure_attach.video(browser)

    browser.quit()
