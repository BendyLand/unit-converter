import temperature
import distance

print("Hello Unit Converter!")

def test_temperature():
    temp1 = 32
    result1 = temperature.convert_temperature(temp1, "f", "c")
    temp2 = 61
    result2 = temperature.convert_temperature(temp2, "c", "f")
    print(f"{temp1}f = {result1}c")
    print(f"{temp2}c = {result2}f")


def test_distance():
    dist1 = 2735
    result1 = distance.convert_distance(dist1, "ft", "km")
    dist2 = 47
    result2 = distance.convert_distance(dist2, "yard", "in")
    dist3 = 1241
    result3 = distance.convert_distance(dist3, "mm", "yd")
    dist4 = 1
    result4 = distance.convert_distance(dist3, "mi", "mm")
    print(f"{dist1}ft = {result1}km")
    print(f"{dist2}yd = {result2}in")
    print(f"{dist3}mm = {result3}yd")
    print(f"{dist4}mi = {result4}mm")


def main():
    test_temperature()
    test_distance()


if __name__ == "__main__":
    main()

"""
2DO:
    Mass/Weight:
        Gram (g)
        Kilogram (kg)
        Milligram (mg)
        Ton (t)
        Pound (lb)
        Ounce (oz)    
    Time:
        Second (s)
        Minute (min)
        Hour (h)
        Day
        Week
        Month
        Year
    Volume:
        Liter (L)
        Milliliter (mL)
        Cubic meter (m³)
        Gallon (gal)
        Quart (qt)
        Pint (pt)
        Fluid ounce (fl oz)
    Area:
        Square meter (m²)
        Square kilometer (km²)
        Square centimeter (cm²)
        Hectare (ha)
        Acre
    Speed:
        Meters per second (m/s)
        Kilometers per hour (km/h)
        Miles per hour (mph)
"""