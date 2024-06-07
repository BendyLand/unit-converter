import temperature
import distance
import mass
import my_time

def test_my_time():
    time1 = 50
    time2 = 6
    time3 = 36709
    res1 = my_time.convert_time(time1, "day", "second")
    res2 = my_time.convert_time(time2, "h", "month")
    res3 = my_time.convert_time(time3, "s", "day")
    print(f"{time1}day = {res1}s")
    print(f"{time2}h = {res2}month")
    print(f"{time3}s = {res3}day")


def test_mass():
    mass1 = 8
    mass2 = 150
    mass3 = 2
    res1 = mass.convert_mass(mass1, "g", "mg")
    res2 = mass.convert_mass(mass2, "oz", "g")
    res3 = mass.convert_mass(mass3, "t", "lb")
    print(f"{mass1}g = {res1}mg")
    print(f"{mass2}oz = {res2}g")
    print(f"{mass3}t = {res3}lb")


def test_temperature():
    temp1 = 61
    temp2 = 11
    res1 = temperature.convert_temperature(temp1, "f", "c")
    res2 = temperature.convert_temperature(temp2, "c", "f")
    print(f"{temp1}f = {res1}c")
    print(f"{temp2}c = {res2}f")


def test_distance():
    dist1 = 2735
    dist2 = 47
    dist3 = 1241
    dist4 = 1
    res1 = distance.convert_distance(dist1, "ft", "km")
    res2 = distance.convert_distance(dist2, "yard", "in")
    res3 = distance.convert_distance(dist3, "mm", "yd")
    res4 = distance.convert_distance(dist3, "mi", "mm")
    print(f"{dist1}ft = {res1}km")
    print(f"{dist2}yd = {res2}in")
    print(f"{dist3}mm = {res3}yd")
    print(f"{dist4}mi = {res4}mm")
