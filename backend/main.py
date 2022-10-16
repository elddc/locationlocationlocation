from cgi import test
from location import Location
import power

test_place = Location(39.166605, -89.465, 1500)
print(test_place.weather_df['pres'])
print(test_place.get_avg_barometric_pressure())
print(test_place.get_avg_humidity())
print(test_place.get_avg_air_temp())
print(test_place.air_density)
test_power = power.power(test_place)
print(test_power.get_solar_power())
print(test_power.get_wind_power())
print(test_power.get_nuclear_power())
print(test_place.get_avg_wind_speed())