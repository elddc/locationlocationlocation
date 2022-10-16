from location import Location
from metpy.units import units
import numpy as np
class power:
    def __init__(self, location : Location):
        self.location = location
        self.solar = self.get_solar_power()
        self.wind = self.get_wind_power()
        self.nuclear = self.get_nuclear_power()
        self.corn = self.get_corn_power()
    def get_solar_power(self) -> float:
        """
        """
        return self.location.solar_df['P'].mean() / 1000
    def get_wind_power(self) -> float:
        """
        """
        #Assuming HAWT, Rotor diameter of 90 meters, Vestas V-90 2.0 MW turbine (which requires about 52 sq m of land)
        #https://www.vestas.com/en/products-and-solutions/wind-turbines/vestas-v90-2-mw
        # Project Development Report Bartlett Towers By Prosim Power Virginia Tech 
        
        swept_area = np.pi * (90/2)**2
        land_req = 52 
        num_turbines = np.floor(self.location.area / land_req)
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
        return real_power / 1000000
    def get_nuclear_power(self) -> float:
        land_ratio = (1000 / 1.3 * units('MW / mi^2')).to('MW / m^2')
        output = self.location.area * units('m^2') * land_ratio
        output_as_float = float(str(output).replace("megawatt", ""))
        return output_as_float
    def get_corn_power(self) -> float:
        """
        """
        gals_per_square_meter = 328 / 4047
        return self.location.area * gals_per_square_meter / 3412000 * 8760
    def sort_power(self) -> list:
        """
        """
        sorted = sorted([self.solar, self.wind, self.nuclear, self.corn], reverse=True)
        return 

