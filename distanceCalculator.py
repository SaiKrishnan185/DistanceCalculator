from math import radians, asin, sqrt, cos, sin


# Calculate distance between latitude and longitude

def distance(lt1, lg1, lt2, lg2):
    lt1 = radians(lt1)
    lt2 = radians(lt2)
    lg1 = radians(lg1)
    lg2 = radians(lg2)
    # print(lt1,lt2,lg1,lg2)
    lg_distance = lg2 - lg1
    lt_distance = lt2 - lt1
    res = sin(lt_distance / 2) ** 2 + cos(lt1) * cos(lt2) * sin(lg_distance / 2) ** 2
    ct = 2 * asin(sqrt(res))

    radius = 6371

    # print(round(ct * radius, 2))
    return round(ct * radius, 2)
    # return float(f'{ct * radius:.2f}')