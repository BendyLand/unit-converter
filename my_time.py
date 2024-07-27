def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "second":
            result = "s"
        case "minute":
            result = "min"
        case "hour":
            result = "h"
        case _:
            result = unit
    return result


def normalize(num, unit):
    result = 0
    unit = abbreviate(unit)
    match unit:
        case "s":
            result = num / 3600
        case "min":
            result = num / 60
        case "h":
            result = num
        case "day":
            result = num * 24
        case "week":
            result = num * 168
        case "month":
            result = num * 730
        case "year":
            result = num * 8760
        case _:
            print(f"Unrecognized unit: '{unit}'")
            raise ValueError
    return result


def convert_time(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "s":
            result = num * 3600
        case "min":
            result = num * 60
        case "h":
            result = num
        case "day":
            result = num / 24
        case "week":
            result = num / 168
        case "month":
            result = num / 730
        case "year":
            result = num / 8760
    result = round(result, 2)
    return result
