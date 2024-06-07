def abbreviate(unit):
    result = ""
    match unit:
        case "meter":
            result = "m"
        case "kilometer":
            result = "km"
        case "centimeter":
            result = "cm"
        case "millimeter":
            result = "mm"
        case "inch":
            result = "in"
        case "foot":
            result = "ft"
        case "yard":
            result = "yd"
        case "mile":
            result = "mi"
        case _:
            result = unit
    return result


def check_unit_type(unit):
    metric = ["m", "km", "cm", "mm", "meter", "kilometer", "centimeter", "millimeter"]
    imperial = ["in", "ft", "yd", "mi", "inch", "feet", "yard", "mile"]
    result = ""
    if unit in metric:
        result = "metric"
    elif unit in imperial:
        result = "imperial"
    return result


def normalize(num, unit):
    unit = unit.lower()
    unit = abbreviate(unit)
    result = 0
    unit_type = check_unit_type(unit)
    if unit_type == "metric":
        temp = 0
        match unit:
            case "m": 
                temp = num
            case "km": 
                temp = num * 1000
            case "cm": 
                temp = num / 100
            case "mm": 
                temp = num / 1000
        result = temp
    elif unit_type == "imperial":
        temp = 0
        match unit:
            case "in":
                temp = num / 36
            case "ft":
                temp = num / 3
            case "yd": 
                temp = num 
            case "mi": 
                temp = num * 1760
        result = temp
    else:
        print(f"Unrecognized unit: '{unit}'")
        raise ValueError
    result = round(result, 2)
    return result


def convert_from_imperial(num, to):
    result = 0
    match to:
        case "m":
            result = num / 1.094
        case "km":
            result = num / 1094
        case "cm":
            result = num * 91.44
        case "mm":
            result = num * 914.4
        case "in":
            result = num * 36
        case "ft":
            result = num * 3
        case "yd":
            result = num
        case "mi":
            result = num / 1760
    result = round(result, 2)
    return result


def convert_from_metric(num, to):
    result = 0
    match to:
        case "m":
            result = num
        case "km":
            result = num / 1000
        case "cm":
            result = num * 100
        case "mm":
            result = num * 1000
        case "in":
            result = num * 39.37
        case "ft":
            result = num * 3.281
        case "yd":
            result = num * 1.094
        case "mi":
            result = num / 1609
    result = round(result, 2)
    return result


def convert_distance(num, frm, to):
    num = normalize(num, frm)
    unit_type = check_unit_type(frm)
    match unit_type:
        case "imperial":
            return convert_from_imperial(num, to)
        case "metric":
            return convert_from_metric(num, to)
