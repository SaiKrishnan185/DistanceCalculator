# Created by Sai Krishnan RU
# 16-12-2021

# Sort the dataset with population
# Select values with population limit and having least 1 exclusive currency
# Find sum of length between each of the 20 coordinates
# Radius = 6371 km
# Round length of each line and final result to 2 decimal points
# Set missing coordinates as 0.000 N 0.000 E

from data import details

import distanceCalculator

# for i in details:
#     print(i["population"])

currency_data_d = []
currency_data = []
population_data = []
populationLimit = 31028700

# for i in details:
#     print(i["population"])

# Creating a dataset with unique currencies
for i in details:
    for b in (i["currencies"]):
        currency_count = 0
        for a in details:
            for c in a["currencies"]:
                if (c["code"]) == (b["code"]):
                    currency_count = currency_count + 1

        if currency_count == 1:
            currency_data.append(i)


# print currency and country name for testing
# for i in currency_data:
#     print(i["currencies"][0]["code"], i["currencies"][0]["name"])

# Create new dataset with population limit
for i in currency_data:
    if i["population"] >= populationLimit:
        population_data.append(i)

# for i in population_data:
#     print(i["population"])

# Select 20 countries
final_countries = population_data[0:20]
# print(len(final_countries))

# for i in final_countries:
#     print(i["latlng"])

# Calculating sum of distance
total = 0
final_countries_copy = final_countries.copy()

# for i in final_countries:
#     final_countries_copy.remove(i)
#     # if len(final_countries_copy) != 0:
#     for j in final_countries_copy:
#         total = total + (distanceCalculator.distance(i["latlng"][0], i["latlng"][1], j["latlng"][0], j["latlng"][1]))
# print(round(total, 2))


for i in final_countries:
    final_countries_copy.remove(i)
    # if len(final_countries_copy) != 0:
    for j in final_countries_copy:
        total = total + (distanceCalculator.distance(i["latlng"][0], i["latlng"][1], j["latlng"][0], j["latlng"][1]))
        # break
print(round(total, 2))