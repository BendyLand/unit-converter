import temperature
import distance
import mass
import my_time
import sys
import volume
import test

def display_valid_units():
    temps = ["Temperatures:", "f", "c", "k"]
    dists = ["Distances:", "mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
    masses = ["Masses:", "mg", "g", "kg", "oz", "lb", "t"]
    times = ["Times:", "s", "min", "h", "day", "week", "month", "year"]
    volumes = ["Volumes:", "mL", "L", "m3", "qt", "gal", "ft3"]
    areas = ["Areas:", "in2", "ft2", "yd2", "mi2", "m2", "km2"]
    units = [temps, dists, masses, times, volumes]
    for unit in units:
        for item in unit:
            print(item, end=" ")
        print("")


def check_cl_args():
    args = sys.argv
    if len(args) > 1:
        if "-h" in args or "--help" in args:
            display_valid_units()
            return None, False
        elif "-t" in args or "--test" in args:
            test.run_tests()
            return None, False
        return sys.argv, True
    else:
        return None, False
        
        
def select_conversion(arg):
    temps = ["f", "c", "k"]
    dists = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
    masses = ["mg", "g", "kg", "oz", "lb", "t"]
    times = ["s", "min", "h", "day", "week", "month", "year"]
    volumes = ["mL", "L", "m3", "qt", "gal", "ft3"]
    result = ""
    if arg in temps:
        result = "temperature"
    elif arg in dists:
        result = "distance"
    elif arg in masses:
        result = "mass"
    elif arg in times:
        result = "time"
    elif arg in volumes:
        result = "volume"
    else:
        print("Unknown conversion.")
        raise ValueError
    return result


def convert(args):
    conversion = select_conversion(args[2])
    num = float(args[1])
    unit1 = args[2]
    unit2 = args[3]
    result = ""
    match conversion:
        case "temperature":
            result = temperature.convert_temperature(num, unit1, unit2)
        case "distance":
            result = distance.convert_distance(num, unit1, unit2)
        case "mass":
            result = mass.convert_mass(num, unit1, unit2)
        case "time":
            result = my_time.convert_time(num, unit1, unit2)
        case "volume":
            result = volume.convert_volume(num, unit1, unit2)
    print(f"{args[1]}{unit1} = {result}{unit2}")
