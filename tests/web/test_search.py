from qa_guru_python_diploma.pages.web.base_page import open_main_page
from qa_guru_python_diploma.pages.web.search import click_on_search, type_movie_title, search_result_should_be_visible


def test_find_movie_by_title():
    # GIVEN
    title = 'Хроники риддика'
    open_main_page()

    # WHEN
    click_on_search()
    type_movie_title(title)

    # THEN
    search_result_should_be_visible()
