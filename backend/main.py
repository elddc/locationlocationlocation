from cgi import test
from location import Location
import power

test_place = Location(33.756217, -84.436407, 20)
test_power = power.power(test_place)
print(test_power.get_solar_power())
print(test_power.get_wind_power())
print(test_power.get_nuclear_power())