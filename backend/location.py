import datetime
import pandas as pd
import numpy as np 
import meteostat
import pvlib
class Location:
    """
    Location that user picked and the weather + solar parameters for that location
    """
    def __init__(self, lat, lon, radius):
        self.lat = lat
        self.lon = lon
        self.radius = radius
        self.area = 0.0
        self.weather_df = None
        self.solar_df = None
        self.start = datetime(2000, 1, 1)
        self.end = datetime(2021, 12, 31)
        self.get_area()
        self.get_weather_data()
        self.get_solar_data()
    def get_area(self):
        """
        Calculate the area of the circle
        """
        self.area = np.pi * self.radius**2
    def get_weather_data(self):
        """
        """
        station = meteostat.Point(self.lat, self.lon).nearest_stations().fetch(1)
        
        monthly_data = meteostat.Monthly(station, self.start, self.end).fetch()
        average_values = monthly_data.mean()
        self.weather_df = pd.DataFrame(average_values)
    def get_solar_data(self):
        """
        """
        # assuming conversion efficiency of 15% for solar panels
        peakpower = self.area * 0.15
        df = pvlib.iotools.get_pvgis_hourly(self.lat, self.lon, self.start, self.end,pvcalculation=True, peakpower=peakpower, loss=26.0, map_variables=True)
        self.solar_df = df
    def get_avg_irradiance(self) -> float:
        """
        """
        return 0.0
    def get_avg_air_temp(self) -> float:
        """
        """
        return 0.0
    def get_avg_humidity(self) -> float:
        """
        """
        return 0.0
    def get_avg_barometric_pressure(self) -> float:
        """
        """
        return 0.0
    def get_altitude(self) -> float:
        """
        """
        return 0.0
    def get_avg_wind_speed(self) -> float:
        """
        """
        return 0.0
    def get_avg_air_density(self) -> float:
        """
        """
        return 0.0
        