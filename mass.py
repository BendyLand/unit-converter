def abbreviate(unit):
    result = ""
    match unit:
        case "gram":
            result = "g"
        case "kilogram":
            result = "kg"
        case "milligram":
            result = "mg"
        case "ton":
            result = "t"
        case "pound":
            result = "lb"
        case "ounce":
            result = "oz"
        case _:
            result = unit
    return result


def check_unit_type(unit):
    metric = ["g", "kg", "mg"]
    imperial = ["t", "lb", "oz"]
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
        match unit:
            case "mg":
                result = num / 1000
            case "g":
                result = num
            case "kg":
                result = num * 1000
    elif unit_type == "imperial":
        match unit:
            case "oz":
                result = num / 16
            case "lb":
                result = num
            case "t":
                result = num * 2000
    else:
        print(f"Unrecognized unit: '{unit}'")
        raise ValueError
    result = round(result, 2)
    return result


def convert_from_imperial(num, to):
    result = 0
    match to:
        case "mg":
            result = num * 453600
        case "g":
            result = num * 453.6
        case "kg":
            result = num / 2.205
        case "oz":
            result = num * 16
        case "lb":
            result = num
        case "t":
            result = num / 2000
    result = round(result, 2)
    return result


def convert_from_metric(num, to):
    result = 0
    match to:
        case "mg":
            result = num * 1000
        case "g":
            result = num
        case "kg":
            result = num / 1000
        case "oz":
            result = num / 28.35
        case "lb":
            result = num / 453.6
        case "t":
            result = num / 907200
    result = round(result, 2)
    return result


def convert_mass(num, frm, to):
    num = normalize(num, frm)
    unit_type = check_unit_type(frm)
    match unit_type:
        case "imperial":
            return convert_from_imperial(num, to)
        case "metric":
            return convert_from_metric(num, to)


