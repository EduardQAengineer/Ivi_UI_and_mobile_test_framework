from qa_guru_python_diploma.pages.mobile import my_ivi


def test_serials_sections_should_be_shown():
    # WHEN
    my_ivi.tap_on_my_ivi()

    # THEN
    my_ivi.serials_should_be_shown()


def test_select_movie_in_recommends():
    # WHEN
    my_ivi.tap_on_recommend_movie()

    # THEN
    my_ivi.button_watch_should_be_shown()
