# Unit Converter

*This tool is still under development, and is only partially functional.*

A general purpose unit converter which can convert between various units of:
 - Temperature
 - Distance
 - Weight/Mass
 - Time
 - Volume
 - ~~Area~~
 - ~~Speed~~

(The units which are crossed out have not been implemented yet.)

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
```
