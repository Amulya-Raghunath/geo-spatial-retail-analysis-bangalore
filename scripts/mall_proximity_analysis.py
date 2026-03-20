# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:34:26 2026

@author: Amulya Raghunath
"""

import pandas as pd
from geopy.distance import geodesic
results=[]
shops=pd.read_csv("data/osm_shops_bengaluru.csv")
population=pd.read_csv("data/bengaluru_population.csv")
malls=pd.read_csv("data/bengaluru_shopping_malls.csv")
for _,mall in malls.iterrows():
    mall_location=(mall['latitude'],mall['longitude'])
    nearby_shops=0
    for _,shop in shops.iterrows():
        shop_location=(shop['latitude'],shop['longitude'])
        distance=geodesic(mall_location,shop_location).km
        if distance <=1:
            nearby_shops+=1
    results.append({"mall_name":mall['mall_name'],"area":mall['area'],'nearby_shop_under_1km':nearby_shops})
df=pd.DataFrame(results)
print(df)
df.to_csv("data/mall_shop_density.csv")