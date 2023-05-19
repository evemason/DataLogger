import pandas as pd
from pandas import *


data = pd.read_csv(r'C:\Users\lizzi\DataLogger\Interface_Code\Database\Plant_data.csv')

print(data)
Categories = ["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"]

water_high = data['water_high'].tolist()
water_low = data['water_low'].tolist()
temp_high = data['temp_high'].tolist()
temp_low = data['temp_low'].tolist()
light_high = data['light_high'].tolist()
light_low = data['light_low'].tolist()


def extract_data(plant_name):
    index = Categories.index(plant_name)
    water_level_high = water_high[index]
    water_level_low = water_low[index]
    temp_level_low = temp_low[index]
    temp_level_high = temp_high[index]
    light_level_low = light_low[index]
    light_level_high = light_high[index]

    print(water_level_high, water_level_low, temp_level_high, temp_level_low, light_level_high, light_level_low)


extract_data("Cactus")


