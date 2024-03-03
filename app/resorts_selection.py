from math import *


def find_nearest_resorts(lat_city, lon_city):
    data = []
    distances_list = []
    lowest_5_data = []

    with open('north_american_resorts.csv', 'r') as infile:
        next(infile)
        for line in infile:
            new_line = line.split(',')
            lat = radians(float(new_line[3]))
            lon = radians(float(new_line[4]))
            distance = acos(sin(lat_city)*sin(lat)+cos(lat_city)*cos(lat)*cos(lon-lon_city))*6371
            distances_list.append(distance)
            temp_list = [distance, new_line[0], new_line[1], new_line[3], new_line[4], new_line[5],
                         new_line[10], new_line[21]]
            data.append(temp_list)

    for _ in range(5):
        min_index = distances_list.index(min(distances_list))
        lowest_5_data.append(data[min_index])
        del data[min_index]
        del distances_list[min_index]

    return lowest_5_data
