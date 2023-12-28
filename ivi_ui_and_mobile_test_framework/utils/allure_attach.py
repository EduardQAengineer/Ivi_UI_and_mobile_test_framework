import allure
import requests


def bstack_video(session_id):
    from config import config as app_config
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(app_config.userName, app_config.accessKey)
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML
    )


def page_source_xml(browser):
    allure.attach(
        browser.driver.page_source,
        name='page_source_xml',
        attachment_type=allure.attachment_type.XML
    )


def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )

def logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(
        body=log,
        name='browser_logs',
        attachment_type=allure.attachment_type.TEXT,
        extension='.log'
    )

def html(browser):
    source_html = browser.driver.page_source
    allure.attach(
        body=source_html,
        name='page_source',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )

def video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html_markup = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html_markup,
        name='video_' + browser.driver.session_id,
        attachment_type=allure.attachment_type.HTML,
        extension='.html')
