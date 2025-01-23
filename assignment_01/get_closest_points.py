from haversine import haversine


class InvalidInputException(Exception):
    pass


def get_closest_points(geolocations_1: list[tuple[float, float]],
                       geolocations_2: list[tuple[float, float]]) -> list[int]:
    """Match each point in the first array
    to the closest one in the second array

    Args:
        geolocations_1 (list[tuple[float, float]]): A list of tuples containing
                                                    latitude and longitude

        geolocations_2 (list[tuple[float, float]]): A list of tuples containing
                                                    latitude and longitude

    Raises:
        InvalidInputException: At least one input list is invalid

    Returns:
        list[int]: A list of integers where the point in the second array
        indexed by the integer is the closest point from the second array
        to the point in the first array indexed by the integer's index.
    """
    if (len(geolocations_1) == 0 or len(geolocations_2) == 0):
        raise InvalidInputException(
            "Both input lists must have at least one entry"
        )

    if (not all(
            type(obj) is tuple and len(obj) == 2
            for obj in geolocations_1 + geolocations_2
            )):
        raise InvalidInputException(
            "All elements in both lists must be a tuple of size 2"
        )

    if (not all(
            type(latitude) in (int, float) or type(longitude) in (int, float)
            for (latitude, longitude) in geolocations_1 + geolocations_2
            )):
        raise InvalidInputException(
            "Latitude and longitude must be either integers or floats"
        )

    if (not all(
            -90 <= latitude <= 90 and -90 <= longitude <= 90
            for (latitude, longitude) in geolocations_1 + geolocations_2
            )):
        raise InvalidInputException(
            "Latitude and longitude must be between -90 and 90"
        )

    min_distances = [float("inf") for _ in geolocations_1]
    index_list = [0 for _ in geolocations_1]

    for reference_idx, reference_point in enumerate(geolocations_1):
        for comparison_idx, comparison_point in enumerate(geolocations_2):
            current_distance = haversine(reference_point, comparison_point)

            if (current_distance < min_distances[reference_idx]):
                min_distances[reference_idx] = current_distance
                index_list[reference_idx] = comparison_idx

    return index_list
