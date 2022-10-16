from location import Location
from metpy.units import units
import numpy as np
class power:
    def __init__(self, location : Location):
        self.location = location
    def get_solar_power(self) -> float:
        """
        """
        return self.location.solar_df['P'].mean() / 1000 * units('MW')
    def get_wind_power(self) -> float:
        """
        """
        #Assuming HAWT, Rotor diameter of 90 meters, Vestas V-90 2.0 MW turbine (which requires about 52 sq m of land)
        #https://www.vestas.com/en/products-and-solutions/wind-turbines/vestas-v90-2-mw
        # Project Development Report Bartlett Towers By Prosim Power Virginia Tech 
        
        swept_area = np.pi * (90/2)**2
        land_req = 52 * units('m^2')
        num_turbines = self.location.area / land_req
        ideal_power_per_turbine = 0.5 * self.location.air_density * swept_area * (self.location.get_avg_wind_speed()**3)
        
        #real efficiency from https://www.omnicalculator.com/ecology/wind-turbine#:~:text=Calculate%20the%20available%20wind%20power,change%20it%20in%20advanced%20mode)
        turbine_efficiency = 0.3
        wake_losses = 0.1
        mechanical_losses = 0.03
        turbine_electrical_losses = 0.015
        trans_electrical_losses = 0.1
        time_ooo = 0.03
        
        real_efficiency = turbine_efficiency * (1 - wake_losses) * (1 - mechanical_losses) * (1 - turbine_electrical_losses) * (1 - trans_electrical_losses) * (1 - time_ooo)
        
        real_power_per_turbine = ideal_power_per_turbine * real_efficiency
        real_power = real_power_per_turbine * num_turbines
        return real_power.to('MW')
    def get_nuclear_power(self) -> float:
        """
        """
        return 0.0
    def get_geothermal_power(self) -> float:
        """
        """
        return 0.0
    