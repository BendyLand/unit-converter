
def check_unit_type(unit):
    metric = ["L", "mL", "m3"]
    imperial = ["gal", "qt", "ft3"]
    result = ""
    if unit in metric:
        result = "metric"
    elif unit in imperial:
        result = "imperial"
    return result


def abbreviate(unit):
    if len(unit) > 3:
        unit = unit.lower()
    result = ""
    match unit:
        case "liter":
            result = "L"
        case "milliliter":
            result = "mL"
        case "cubic meter":
            result = "m3"
        case "gallon":
            result = "gal"
        case "quart":
            result = "qt"
        case "cubic foot":
            result = "ft3"
        case _:
            result = unit
    return result


def normalize(num, unit):
    unit = abbreviate(unit)
    result = 0
    match unit:
        case "L":
            result = num * 1000
        case "mL":
            result = num 
        case "m3":
            result = num * 1000000
        case "gal":
            result = num * 3785
        case "qt":
            result = num * 946.4
        case "ft3":
            result = num * 28320
        case _:
            print(f"Unrecognized unit: '{unit}'")
    return result
    
    
def convert_volume(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "L":
            result = num / 1000
        case "mL":
            result = num 
        case "m3":
            result = num / 1000000
        case "gal":
            result = num / 3785
        case "qt":
            result = num / 946.4
        case "ft3":
            result = num / 28320
    result = round(result, 3)
    return result
