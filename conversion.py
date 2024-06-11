import temperature
import distance
import mass
import my_time
import sys


def check_cl_args():
    if len(sys.argv) == 4:
        return sys.argv, True
    else:
        return None, False


def select_conversion(arg):
    temps = ["f", "c", "k"]
    dists = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
    masses = ["mg", "g", "kg", "oz", "lb", "t"]
    times = ["s", "min", "h", "day", "week", "month", "year"]
    result = ""
    if arg in temps:
        result = "temperature"
    elif arg in dists:
        result = "distance"
    elif arg in masses:
        result = "mass"
    elif arg in times:
        result = "time"
    else:
        print("Unknown conversion.")
        raise ValueError
    return result


def convert(args):
    conversion = select_conversion(args[2])
    num = int(args[1])
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
    print(f"{args[1]}{unit1} = {result}{unit2}")
