from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_movie_sections_should_be_shown():
    # WHEN
    with step('Tap on "Мой ivi"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мой ivi"]')).click()

    # THEN
    with step('Check movie sections'):
        with step('Best shows on subscription - are shown'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Лучшие сериалы в подписке"]')).should(have.text('Лучшие сериалы в подписке'))

        with step('High-rated subscription serials - are shown'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Сериалы с высоким рейтингом по подписке"]')).should(have.text('Сериалы с высоким рейтингом по подписке'))

    # browser.element((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="ru.ivi.client:id/ui_kit_navigation_view"]/android.widget.LinearLayout/android.widget.FrameLayout[2]')).click()
    # browser.element((AppiumBy.ID, 'ru.ivi.client:id/search_input')).wait_until(be.visible)
    # browser.element((AppiumBy.ID, 'ru.ivi.client:id/search_input')).type('Chronical of Riddic')
    # browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Хроники Риддика"]')).wait_until(be.visible)
    # browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Хроники Риддика"]')).should(have.text('Хроники Риддика'))

    #
    # with step('Type search'):
    #     browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
    #     browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Android')
    #
    # # THEN
    # with step('Verify content found'):
    #     results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    #     results.wait_until(be.visible)
    #     results.should(have.size_greater_than(0))
    #     results.first.should(have.text('Android'))