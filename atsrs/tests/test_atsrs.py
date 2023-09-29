from atsrs import Loader


def test_one_from_string():
    Alert = Loader().one_from_bytes(
        b"""
        interface Alert {
          error: boolean;
        }
        """,
    )

    assert Alert(error=False).error == False  # noqa: E712


def test_one_from_string_optional_attr():
    Alert = Loader().one_from_bytes(
        b"""
        interface Alert {
          error: boolean;
          title?: boolean;
        }
        """,
    )

    assert Alert(error=True).title is None
