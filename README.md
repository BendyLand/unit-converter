# Unit Converter

A general purpose unit converter which can convert between various units of:
 - Temperature
 - Distance
 - Weight/Mass
 - Time
 - Volume
 - Area
 - Speed

**Note: This tool is meant for 'quick and dirty' conversions.** 
**It is *not* going to be the most accurate option.**
**Please do not use this tool for important or sensitive operations.**

## Usage

You could package this as an executable file and add it to your path, but personally, I found it easier to just create an alias: 
```shell
alias uc='python3 /absolute/path/to/unit-converter/script.py'
```
Then it can be called like so:
```shell
uc <value> <unit_from> <unit_to>

# Temperature
uc 0 c f        # 0c    = 32.0f (freezing temp)
uc 98.6 f c     # 98.6f = 37.0c (human body temp)

# Distance
uc 26.2 mi km   # 26.2mi   = 42.15km (marathon distance)
uc 8848.86 m ft # 8848.86m = 29033.11ft (height of Mt. Everest)
uc 100 yd m     # 100yd    = 91.41m (length of American Football field)

# Weight/Mass
uc 70 kg lb     # 70kg    = 154.32lb (average human weight)
uc 12000 lb t   # 12000lb = 6.0t (average elephant weight)
uc 12.4 kg lb   # 12.4kg  = 27.34lb (standard gold bar weight)

# Time
uc 24 h min     # 24h    = 1440.0min (1 day in minutes)
uc 1 year day   # 1year  = 365.0day (1 year in days)
uc 8.3 min s    # 8.3min = 498.0s (time for light to travel from Sun to Earth)

# Volume
uc 1 L mL  # 1L = 1000.0mL (Liter to milliliter)
uc 1 gal L # 1gal = 3.785L (US gallon to liter)
uc 1 m3 L  # 1m3 = 1000.0L (Cubic meter to liter)

# Area
uc 1 m2 ft2  # 1m2 = 10.76ft2 (Square meter to square foot)
uc 1 mi2 km2 # 1mi2 = 2.59km2 (Square mile to square kilometer)
uc 9 ft2 yd2 # 9ft2 = 1.0yd2 (9 square feet to a square yard)

# Speed
uc 1 m/s km/h   # 1m/s = 3.6km/h (1 meter per second in km per hour)
uc 1 m/s mph    # 1m/s = 2.24mph (1 meter per second in miles per hour)
uc 60 mph km/h  # 60mph = 96.56km/h (Common travel speeds...)
uc 100 km/h mph  # 100km/h = 62.14mph (...Between mph and km/h)
```
