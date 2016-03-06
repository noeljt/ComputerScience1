"""
A program to determine the amount of rain needed to sustain the Panama Canal.

Author: Joe Noel (noelj)
"""
width = 32
length = 320
depth = 10

def volume_solid(width, length, depth): #returns volume of water needed to fill a lock of these given dimensions
    volume = width * length * depth
    return volume

def water_needed_perlock(volume): #returns amount of water needed to fill lock with given volume for a full year
    ships_per_day = 35
    return ships_per_day * volume * 365

total_volume = 2 * water_needed_perlock(volume_solid(width, length, depth))
rain_needed = float(total_volume) / (9*30)
rain_mm = rain_needed / 600000

print "Panama canal statistics:"
print "The total volume of water needed in Gatun lake:", total_volume, "m^3"
print "In rainy season, daily rain should be at least", int(rain_needed), "m^3"
print "This means, it rains about", rain_mm, "milimeters every day during the rainy season"