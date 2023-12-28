def abs_path_from_project(relative_path: str):
    import ivi_ui_and_mobile_test_framework
    from pathlib import Path

    return (
        Path(ivi_ui_and_mobile_test_framework.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
