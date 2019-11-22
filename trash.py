
import copy, math, random

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    a = road_map[0][2]
    b = road_map[0][3]
    sum_ = 0

    for i in range(0, len(road_map)):
        next_ = road_map[(i + 1) % len(road_map)]
        A, B = a, b
        a, b = next_[2], next_[3]
        sum_ += pythagoras(A, B, a, b)

    return sum_

def pythagoras(A, B, a, b):
    return math.sqrt(((A - a) ** 2) + ((B - b) ** 2))

road_map = [('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122), ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167), ('Connecticut', 'Hartford', 41.767, -72.677)]
"""
, ('Delaware', 'Dover', 39.161921, -75.526755), ('Florida', 'Tallahassee', 30.4518, -84.27277), ('Georgia', 'Atlanta', 33.76, -84.39), ('Hawaii', 'Honolulu', 21.30895, -157.826182), ('Idaho', 'Boise', 43.613739, -116.237651), ('Illinois', 'Springfield', 39.78325, -89.650373), ('Indiana', 'Indianapolis', 39.790942, -86.147685), ('Iowa', 'Des Moines', 41.590939, -93.620866), ('Kansas', 'Topeka', 39.04, -95.69), ('Kentucky', 'Frankfort', 38.197274, -84.86311), ('Louisiana', 'Baton Rouge', 30.45809, -91.140229), ('Maine', 'Augusta', 44.323535, -69.765261), ('Maryland', 'Annapolis', 38.972945, -76.501157), ('Massachusetts', 'Boston', 42.2352, -71.0275), ('Michigan', 'Lansing', 42.7335, -84.5467), ('Minnesota', 'Saint Paul', 44.95, -93.094), ('Mississippi', 'Jackson', 32.32, -90.207), ('Missouri', 'Jefferson City', 38.572954, -92.189283), ('Montana', 'Helana', 46.595805, -112.027031), ('Nebraska', 'Lincoln', 40.809868, -96.675345), ('Nevada', 'Carson City', 39.160949, -119.753877), ('New Hampshire', 'Concord', 43.220093, -71.549127), ('New Jersey', 'Trenton', 40.221741, -74.756138), ('New Mexico', 'Santa Fe', 35.667231, -105.964575), ('New York', 'Albany', 42.659829, -73.781339), ('North Carolina', 'Raleigh', 35.771, -78.638), ('North Dakota', 'Bismarck', 48.813343, -100.779004), ('Ohio', 'Columbus', 39.962245, -83.000647), ('Oklahoma', 'Oklahoma City', 35.482309, -97.534994), ('Oregon', 'Salem', 44.931109, -123.029159), ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613), ('Rhode Island', 'Providence', 41.82355, -71.422132), ('South Carolina', 'Columbia', 34.0, -81.035), ('South Dakota', 'Pierre', 44.367966, -100.336378), ('Tennessee', 'Nashville', 36.165, -86.784), ('Texas', 'Austin', 30.266667, -97.75), ('Utah', 'Salt Lake City', 40.7547, -111.892622), ('Vermont', 'Montpelier', 44.26639, -72.57194), ('Virginia', 'Richmond', 37.54, -77.46), ('Alabama', 'Montgomery', 32.361538, -86.279118), ('West Virginia', 'Charleston', 38.349497, -81.633294), ('Wisconsin', 'Madison', 43.074722, -89.384444), ('Wyoming', 'Cheyenne', 41.145548, -104.802042), ('Washington', 'Olympia', 47.042418, -122.893077)]
"""
print(road_map)
print(compute_total_distance(road_map))
index1 = 1
index2 = 5



road_ = copy.copy(road_map) #This copy is necessary
road_[index1], road_[index2] = road_[index2], road_[index1]

new_total_distance = compute_total_distance(road_)

print(road_, new_total_distance) #this needs to be tested (not sure what)
