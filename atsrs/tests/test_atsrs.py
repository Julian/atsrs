from atsrs import Loader


def test_one_from_string():
    Alert = Loader().one_from_string(
        """
        interface Alert {
          error: boolean;
        }
        """,
    )

    Alert(error=False)
