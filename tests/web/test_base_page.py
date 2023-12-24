from selene import browser, have, be


def test_open_base_page():
    browser.open('/')
    # browser.element('.nbl-controlButton__caption').should(be.visible).click()
    browser.element('#headerTop').should(have.text('Мой Иви'))


def test_search():
    browser.open('/')
    # browser.element('.nbl-controlButton__caption').should(be.visible).click()
    browser.element('[data-test="header_search"]').should(be.visible).click()
    browser.element('input[data-test="search_input"]').type('Хроники риддика').press_enter()
    browser.element('.searchBlock.searchBlock_result').should(have.text('Также смотрят'))


def test_open_move():
    browser.open('/')
    # browser.element('.nbl-controlButton__caption').should(be.visible).click()
    browser.element('[data-content-id="16974"]').should(be.visible).click()
    browser.element('[data-testid="watchTitle"]').should(have.text('Сериал Блеск смотреть онлайн'))
