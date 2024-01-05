import math


def cumulative_elevation_gain(points):
    """
    Calculates the cumulative elevation gain for a list of points.
    Points should be a list of tuples in the format (altitude, distance).
    """
    cumulative_gain = 0
    for i in range(len(points) - 1):
        altitude_diff = points[i + 1][0] - points[i][0]
        distance = points[i + 1][1] - points[i][1]
        cumulative_gain += altitude_diff * distance / 1000  # Convert to meters
    return cumulative_gain


if __name__ == "__main__":
    # Prompt the user to enter the starting altitude
    starting_altitude = float(input("Enter the starting altitude: "))

    # Loop until the user enters 'quit'
    points = []
    while True:
        # Prompt the user to enter the next point
        point = input("Enter a point (format: altitude, distance): ")
        if point.lower() == "quit":
            break
        point_data = point.split(",")
        if len(point_data) != 2:
            print("Invalid point format")
            continue
        altitude = float(point_data[0])
        distance = float(point_data[1])
        points.append((altitude, distance))

    # Calculate the cumulative elevation gain and print the result
    cumulative_gain = cumulative_elevation_gain(points)
    print(f"The cumulative elevation gain is {cumulative_gain:.2f} meters.")
