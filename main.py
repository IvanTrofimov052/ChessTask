size = 100
size_of_novosibirsk = 178200000000 # in meters
size_of_russia = 178200000000 # in meters
speed_russia = 106000000
speed_novosibirsk = 2300000


# In this function we consider how many corn we must have
def how_many_corn(territory_size):
    answer = 1
    i = 0
    while i < territory_size:
        answer *= 2
        i += 1

    return answer


# This function need to meter how corn is weight
def how_many_corn_is_weight(number_of_corn):
    return number_of_corn * 50 / 1000 / 1000 / 1000


# this function for task number 3
# the returned data in santimeters
def height_territory(territory_size, number_of_corn):
    return int(number_of_corn * 0.0000002 // territory_size) * 0.0009


def how_many_years_need_to_collect_wheat(speed, weight):
    return weight / speed


print(how_many_corn(size))
print(str(how_many_corn_is_weight(how_many_corn(size))) + " тонн")
print(str(height_territory(size_of_russia, how_many_corn(size))) + ' метров')
print(str(height_territory(size_of_russia, how_many_corn(size))) + ' метров')
