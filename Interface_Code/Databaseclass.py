import pandas as pd

class Database:
    data = pd.read_csv(r'Database\Plant_data.csv')
    Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
    def __init__(self, name, water_level_high, water_level_low, temp_level_high, temp_level_low, light_level_high, light_level_low):
        self.name = name 
        self.water_level_high = water_level_high
        self.water_level_low = water_level_low
        self.temp_level_high = temp_level_high
        self.temp_level_low = temp_level_low
        self.moisture_level_high = light_level_high
        self.moisture_level_low = light_level_low
    def water_level_high(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        water_high = data['water_high'].tolist()
        return water_high[index]
    def water_level_low(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        water_low = data['water_low'].tolist()
        return water_low[index]
    def temp_level_high(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        temp_high = data['temp_high'].tolist()
        return temp_high[index]
    def temp_level_low(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        temp_low = data['temp_low'].tolist()
        return temp_low[index]
    def light_level_high(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        light_high = data['light_high'].tolist()
        return light_high[index]
    def light_level_low(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        light_low = data['light_low'].tolist()
        return light_low[index]
    def extract_all(name):
        data = pd.read_csv(r'Database\Plant_data.csv')
        Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
        index = Categories.index(name)
        water_high = data['water_high'].tolist()
        water_low = data['water_low'].tolist()
        temp_high = data['temp_high'].tolist()
        temp_low = data['temp_low'].tolist()
        light_high = data['light_high'].tolist()
        light_low = data['light_low'].tolist()

        water_level_high = water_high[index]
        water_level_low = water_low[index]
        temp_level_low = temp_low[index]
        temp_level_high = temp_high[index]
        light_level_low = light_low[index]
        light_level_high = light_high[index]
        return water_level_high, water_level_low, temp_level_high, temp_level_low, light_level_high, light_level_low



#y = Database.light_level_high('Alpine')
#print(y)

#x= Database.extract_all('Alpine')
#print(x)