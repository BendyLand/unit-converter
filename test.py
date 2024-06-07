import temperature
import distance

def test_temperature():
    temp1 = 61
    result1 = temperature.convert_temperature(temp1, "f", "c")
    temp2 = 11
    result2 = temperature.convert_temperature(temp2, "c", "f")
    print(f"{temp1}f = {result1}c")
    print(f"{temp2}c = {result2}f")


def test_distance():
    dist1 = 2735
    result1 = distance.convert_distance(dist1, "ft", "km")
    dist2 = 47
    result2 = distance.convert_distance(dist2, "yard", "in")
    dist3 = 1241
    result3 = distance.convert_distance(dist3, "mm", "yd")
    dist4 = 1
    result4 = distance.convert_distance(dist3, "mi", "mm")
    print(f"{dist1}ft = {result1}km")
    print(f"{dist2}yd = {result2}in")
    print(f"{dist3}mm = {result3}yd")
    print(f"{dist4}mi = {result4}mm")