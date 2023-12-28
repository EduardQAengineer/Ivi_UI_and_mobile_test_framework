from qa_guru_python_diploma.pages.web.base_page import open_main_page, my_ivi_at_top_menu_should_be_visible, \
    click_on_movie_preview, movie_title_should_be_visible, click_on_promo, check_promo_title, check_promo_button


def test_open_base_page():
    # GIVEN
    open_main_page()

    # THEN
    my_ivi_at_top_menu_should_be_visible()


def test_open_movie():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_movie_preview()

    # THEN
    movie_title_should_be_visible()


def test_open_promo():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_promo()

    # THEN
    check_promo_title()
    check_promo_button()
