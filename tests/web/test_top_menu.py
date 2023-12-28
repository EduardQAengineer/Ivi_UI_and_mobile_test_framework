from qa_guru_python_diploma.pages.web.base_page import open_main_page
from qa_guru_python_diploma.pages.web.top_menu import click_on_whats_new, check_whats_new_title, click_on_movies, \
    check_movies_title, click_on_serials, check_serials_title, click_on_cartoons, check_cartoons_title


def test_whats_new():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_whats_new()

    # THEN
    check_whats_new_title()


def test_movies():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_movies()

    # THEN
    check_movies_title()

def test_serials():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_serials()

    # THEN
    check_serials_title()

def test_cartoons():
    # GIVEN
    open_main_page()

    # WHEN
    click_on_cartoons()

    # THEN
    check_cartoons_title()
