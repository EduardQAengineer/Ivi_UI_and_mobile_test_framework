from qa_guru_python_diploma.pages.web.base_page import open_main_page
from qa_guru_python_diploma.pages.web.top_menu import TopMenu


top_menu = TopMenu()


def test_whats_new():
    # GIVEN
    open_main_page()

    # WHEN
    top_menu.click_on_whats_new()

    # THEN
    top_menu.check_whats_new_title()


def test_movies():
    # GIVEN
    open_main_page()

    # WHEN
    top_menu.click_on_movies()

    # THEN
    top_menu.check_movies_title()


def test_serials():
    # GIVEN
    open_main_page()

    # WHEN
    top_menu.click_on_serials()

    # THEN
    top_menu.check_serials_title()


def test_cartoons():
    # GIVEN
    open_main_page()

    # WHEN
    top_menu.click_on_cartoons()

    # THEN
    top_menu.check_cartoons_title()
