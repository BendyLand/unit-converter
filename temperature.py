def convert_temperature(frm, to, num):
    result = 0
    if frm == "f":
        if to == "c":
            result = (num - 32) * 5 / 9 # f to c 
        elif to == "k":
            result = ((num - 32) * 5 / 9) + 273.15
        elif to == "f":
            result = num
        else:
            print("Invalid unit.")
    elif frm == "c":
        if to == "f":
            result = (num * 9 / 5) + 32 # c to f 
        elif to == "k":
            result = num + 273.15
        elif to == "c":
            result = num
        else:
            print("Invalid unit.")
    elif frm == "k":
        if to == "f":
            result = (num - 273.15) * 9 / 5 + 32
        elif to == "c":
            result = num - 273.15
        elif to == "k":
            result = num
        else:
            print("Invalid unit. Returning 0...")
    else:
        print("Invalid unit")
    return result