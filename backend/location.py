import datetime
import pandas as pd
import numpy as np 
import meteostat
import pvlib
import requests
import metpy.calc as mpcalc
from metpy.units import units
class Location:
    """
    Location that user picked and the weather + solar parameters for that location
    """
    def __init__(self, lat, lon, radius):
        self.lat = lat
        self.lon = lon
        self.radius = radius
        self.start = datetime.datetime(2010, 1, 1)
        self.end = datetime.datetime(2015, 12, 31)
        self.area = self.get_area()
        self.weather_df = self.get_weather_data()
        self.solar_df = self.get_solar_data()
        self.air_density = self.get_avg_air_density()
    def get_area(self) -> float:
        return np.pi * self.radius**2 
    def get_weather_data(self):
        """
        """
        stations = meteostat.Stations()
        stations = stations.nearby(self.lat, self.lon)
        station = stations.fetch(1)
        
        hourly_data = meteostat.Hourly(station, self.start, self.end).fetch()
        return hourly_data
    def get_solar_data(self):
        """
        """
        # assuming conversion efficiency of 15% for solar panels
        peakpower = self.area * 0.15
        df, _, _= pvlib.iotools.get_pvgis_hourly(latitude=self.lat, longitude=self.lon, start=self.start, end=self.end,pvcalculation=True, peakpower=peakpower, loss=26)
        return df
    def get_avg_air_temp(self):
        """
        """
        return self.weather_df['temp'].mean()
    def get_avg_humidity(self):
        """
        """
        return self.weather_df['rhum'].mean()
    def get_avg_barometric_pressure(self):
        """
        """
        return self.weather_df['pres'].mean()
    def get_altitude(self):
        """
        Adapted from https://stackoverflow.com/questions/19513212/can-i-get-the-altitude-with-geopy-in-python-with-longitude-latitude
        """
        query = ('https://api.open-elevation.com/api/v1/lookup'f'?locations={self.lat},{self.lon}')
        r = requests.get(query).json()  # json object, various ways you can extract value
        # one approach is to use pandas json functionality:
        altitude = pd.json_normalize(r, 'results')['elevation'].values[0]
        return altitude * units('m')
    def get_avg_wind_speed(self):
        """
        """
        return self.weather_df['wspd'].mean() / 3.6
    def get_avg_air_density(self):
        """
        """
        output_in_units = mpcalc.density((self.get_avg_barometric_pressure() * units('hPa')), (self.get_avg_air_temp() * units('celsius')), (self.get_avg_humidity() * units('percent')))
        unitless = float(str(output_in_units).replace('kg / m3', ''))
        return unitless