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
        self.area = 0.0
        self.weather_df = None
        self.solar_df = None
        self.start = datetime.datetime(2005, 1, 1)
        self.end = datetime.datetime(2015, 12, 31)
        self.get_area()
        self.get_weather_data()
        self.get_solar_data()
    def get_area(self):
        """
        Calculate the area of the circle
        """
        self.area = np.pi * self.radius**2 * units('m^2')
    def get_weather_data(self):
        """
        """
        stations = meteostat.Stations()
        stations = stations.nearby(self.lat, self.lon)
        station = stations.fetch(1)
        
        hourly_data = meteostat.Hourly(station, self.start, self.end).fetch()
        self.weather_df = hourly_data
    def get_solar_data(self):
        """
        """
        # assuming conversion efficiency of 15% for solar panels
        peakpower = self.area * 0.15
        df = pvlib.iotools.get_pvgis_hourly(latitude=self.lat, longitude=self.lon, start=self.start, end=self.end)#,pvcalculation=True, peakpower=peakpower, loss=26.0, map_variables=True)
        self.solar_df = df
    def get_avg_irradiance(self) -> float:
        """
        """
        return 0.0
    def get_avg_air_temp(self) -> float:
        """
        """
        return self.weather_df['temp'].mean() * units('celsius')
    def get_avg_humidity(self) -> float:
        """
        """
        return self.weather_df['rhum'].mean() * units('percent')
    def get_avg_barometric_pressure(self) -> float:
        """
        """
        return self.weather_df['pres'].mean() * units('hPa')
    def get_altitude(self) -> float:
        """
        Adapted from https://stackoverflow.com/questions/19513212/can-i-get-the-altitude-with-geopy-in-python-with-longitude-latitude
        """
        query = ('https://api.open-elevation.com/api/v1/lookup'f'?locations={self.lat},{self.lon}')
        r = requests.get(query).json()  # json object, various ways you can extract value
        # one approach is to use pandas json functionality:
        altitude = pd.json_normalize(r, 'results')['elevation'].values[0]
        return altitude * units('m')
    def get_avg_wind_speed(self) -> float:
        """
        """
        return self.weather_df['wspd'].mean() * units('km/h')
    def get_avg_air_density(self) -> float:
        """
        """

        return mpcalc.density(self.get_avg_barometric_pressure(), self.get_avg_air_temp(), self.get_avg_humidity())
        