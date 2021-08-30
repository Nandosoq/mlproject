from distance import haversine


def test_haversine():

    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 27.9580181, -15.73652
    distance = haversine(lon1, lat1, lon2, lat2)

    assert distance != 0
