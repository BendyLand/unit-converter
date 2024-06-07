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
        if to == "c":
            result = (num - 32) * 5 / 9 # f to c 
        elif to == "k":
            result = ((num - 32) * 5 / 9) + 273.15
        elif to == "f":
            result = num
    elif frm == "c":
        if to == "f":
            result = (num * 9 / 5) + 32 # c to f 
        elif to == "k":
            result = num + 273.15
        elif to == "c":
            result = num
    elif frm == "k":
        if to == "f":
            result = (num - 273.15) * 9 / 5 + 32
        elif to == "c":
            result = num - 273.15
        elif to == "k":
            result = num
    return result
