import temperature
import distance
import mass
import my_time
import volume
import area

def test_area():
    print("\nTesting areas:")
    a1 = 10
    a2 = 537
    a3 = 45
    res1 = area.convert_area(a1, "square foot", "square yard")
    res2 = area.convert_area(a2, "in2", "ft2")
    res3 = area.convert_area(a3, "mi2", "km2")
    print(f"{a1}ft^2 = {res1}yd^2")
    print(f"{a2}in^2 = {res2}ft^2")
    print(f"{a3}mi^2 = {res3}km^2")
    

def test_volume():
    print("\nTesting volumes:")
    vol1 = 2
    vol2 = 10000
    vol3 = 10
    res1 = volume.convert_volume(vol1, "cubic foot", "gal")
    res2 = volume.convert_volume(vol2, "gal", "L")
    res3 = volume.convert_volume(vol3, "gal", "qt")
    print(f"{vol1}ft^3 = {res1}gal")
    print(f"{vol2}gal = {res2}L")
    print(f"{vol3}gal = {res3}qt")


def test_my_time():
    print("\nTesting times:")
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
    print("\nTesting masses:")
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
    print("\nTesting temperatures:")
    temp1 = 61
    temp2 = 11
    res1 = temperature.convert_temperature(temp1, "f", "c")
    res2 = temperature.convert_temperature(temp2, "c", "f")
    print(f"{temp1}f = {res1}c")
    print(f"{temp2}c = {res2}f")


def test_distance():
    print("\nTesting distances:")
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


def run_tests():
    test_temperature()
    test_distance()
    test_mass()
    test_my_time()
    test_volume()
    test_area()
    print()
    