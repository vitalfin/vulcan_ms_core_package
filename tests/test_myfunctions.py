from vulcan_ms_core import myfunctions


def test_haversine():
    assert (
        myfunctions.haversine(52.370216, 4.895168, 52.520008, 13.404954)
        == 945793.4375088713
    )


def sum_two_numbers():
    assert myfunctions.sum_two_numbers(1, 2) == 3
