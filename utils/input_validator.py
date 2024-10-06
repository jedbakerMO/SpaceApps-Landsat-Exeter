from math import pi

def input_validator(longitude, latitude):
    if float(longitude) > pi/2 or float(longitude) < -pi/2:
        raise Exception("Not a valid longitude")
    if float(latitude) > pi/4 or float(latitude) < -pi/4:
        raise Exception("Not a valid latitude")




