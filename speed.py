def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "meters per second":
            result = "m/s"
        case "m per second":
            result = "m/s"
        case "kilometers per hour":
            result = "km/h"
        case "km per hour":
            result = "km/h"
        case "miles per hour":
            result = "mph"
        case "mi per hour":
            result = "mph"
        case _:
            result = unit
    return result


def normalize(num, unit):
    result = 0
    match unit:
        case "m/s":
            result = num
        case "km/h":
            result = num / 3.6
        case "mph":
            result = num / 2.237
    return result


def convert_speed(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "m/s":
            result = num
        case "km/h":
            result = num * 3.6
        case "mph":
            result = num * 2.237
    result = round(result, 2)
    return result
