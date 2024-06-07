def validate_units(frm, to):
    units = ["f", "fahrenheit", "c", "celsius", "k", "kelvin"]
    frm = frm.lower()
    to = to.lower()
    return (frm in units) and (to in units)


def abbreviate(unit):
    result = ""
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
    valid_units = validate_units(frm, to)
    if not valid_units:
        raise ValueError
    frm = abbreviate(frm)
    to = abbreviate(to)
    result = 0
    if frm == "f":
        match to:
            case "c":
                result = (num - 32) * 5 / 9 # f to c 
            case "k":
                result = ((num - 32) * 5 / 9) + 273.15
            case "f":
                result = num
    elif frm == "c":
        match to:
            case "f":
                result = (num * 9 / 5) + 32 # c to f 
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
    return result
