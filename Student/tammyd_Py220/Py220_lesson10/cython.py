"""
Exploring Cython

Code with notes

"""

import math
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

def great_circle_raw(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.cos(theta)))
    return radius * c


# function with acos factored out to a function
def calculate_acos(a, b, theta):
    return math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))


def great_circle_acos(lon1, lat1, lon2, lat2):
    radius = 3956  # mile.s
    x = math.pi / 180
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    # c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.cos(theta)))
    # this time cal call the function instead
    c = calculate_Acos(a, b, theta)
    return radius * c


# Another variation. factoring out more
# great circle algorithm with most steps factored out as fuctions

def calculate_x():
    return math.pi / 180.0


def calculate_coordinate(lat, x):
    return (90.0 - lat) * x


def calculate_theta(lon2, lon1, x):
    return (lon2 - lon1) * x


def great_circle_factored(lon1, lat1, lon2, lat2):
    radius = 3956 # miles
    # replaced (x = math.pi / 180) with:
    x = calculate_x()
    # replaced (a = (90.0 - lat1) * (x)) with:
    a = calculate_coordinate(lat1, x)
    # replaced (b = (90.0 - lat2) * (x)) with:
    b = calculate_coordinate(lat2, x)
    # replaced (theta = (lon2 - lon1) * (x)) with:
    theta = calculate_theta(lon2, lon1, x)
    c = calculate_acos(a, b, theta)
    return radius * c
    

if __name__ == "__main__":
    # multiple ways to run this. run each with different interpreters
    great_circle_raw(lon1, lat1, lon2, lat2)
    # great_circle_acos(lon1, lat1, lon2, lat2)
    # great_circle_factored(lon1, lat1, lon2, lat2)
