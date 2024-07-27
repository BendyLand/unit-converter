def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "square yard":
            result = "yd2"
        case "square foot":
            result = "ft2"
        case "square inch":
            result = "in2"
        case "square mile":
            result = "mi2"
        case "square kilometer":
            result = "km2"
        case "square meter":
            result = "m2"
        case _:
            result = unit
    return result


def normalize(num, unit):
    result = 0
    match unit:
        case "yd2":
            result = num * 9
        case "ft2":
            result = num
        case "in2":
            result = num / 144
        case "mi2":
            result = num * 27880000
        case "km2":
            result = num * 10760000
        case "m2":
            result = num * 10.764
    return result


def convert_area(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "yd2":
            result = num / 9
        case "ft2":
            result = num
        case "in2":
            result = num * 144
        case "mi2":
            result = num / 27880000
        case "km2":
            result = num / 10760000
        case "m2":
            result = num / 10.764
        case _:
            print(f"Unknown unit: '{to}'")
    result = round(result, 2)
    return result
