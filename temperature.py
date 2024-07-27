def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "fahrenheit":
            result = "f"
        case "celsius":
            result = "c"
        case "kelvin":
            result = "k"
        case _:
            result = unit
    return result


def convert_temperature(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    result = 0
    if frm == "f":
        match to:
            case "c":
                result = (num - 32) * 5 / 9 
            case "k":
                result = ((num - 32) * 5 / 9) + 273.15
            case "f":
                result = num
    elif frm == "c":
        match to:
            case "f":
                result = (num * 9 / 5) + 32 
            case "k":
                result = num + 273.15
            case "c":
                result = num
    elif frm == "k":
        match to:
            case "f":
                result = (num - 273.15) * 9 / 5 + 32
            case "c":
                result = num - 273.15
            case "k":
                result = num
    result = round(result, 2)
    return result
