from cgi import test
from location import Location
import power

test_place = Location(33.756217, -84.436407, 20)
print(test_place.weather_df)
#print(test_place.get_avg_air_temp())
#print(test_place.get_avg_humidity())
#print(test_place.get_avg_barometric_pressure())



