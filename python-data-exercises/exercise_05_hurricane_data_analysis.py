# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# 1 Update Recorded Damages
def updated_damages(data):
    new_list = []
    for item in data:
        if item == "Damages not recorded":
            new_list.append(item)
        elif "M" in item:
            number = float(item.replace("M", ""))
            new_list.append(number * 1_000_000)
        elif "B" in item:
            number = float(item.replace("B", ""))
            new_list.append(number * 1_000_000_000)
    return new_list
print(updated_damages(damages))

# 2 Create and view the hurricanes dictionary
Cuba_I = {}
for name, month, year, max_sustained_wind, area_affected, updated_damage, death in zip(names, months, years,
                                                                                       max_sustained_winds,
                                                                                       areas_affected,
                                                                                       updated_damages(damages),
                                                                                       deaths):
    Cuba_I[name] = {'Name': name, 'Month': month, 'Year': year, 'Max Sustained Wind': max_sustained_wind,
                    'Areas Affected': area_affected, 'Damage': updated_damage, 'Deaths': death}
print(Cuba_I)


# 3 Organizing by Year
def organize_by_year(hurricanes):
    hurricanes_by_year = {}
    for hurricane in hurricanes.values():
        year = hurricane['Year']
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []
            hurricanes_by_year[year].append(hurricane)
            return hurricanes_by_year


hurricanes_by_year = organize_by_year(Cuba_I)
print(hurricanes_by_year)


# 4 Summing Damaged Areas counts of being stroke
def count_affected_areas(hurricanes):
    area_counts = {}
    for hurricane in hurricanes.values():
        for area in hurricane['Areas Affected']:
            if area not in area_counts:
                area_counts[area] = 1
            else:
                area_counts[area] += 1
    return area_counts


affected_areas = count_affected_areas(Cuba_I)
print(affected_areas)


# 5 Calculating Maximum Hurricane Count to find most frequently affected area and the number of hurricanes involved in
def find_most_affected_area(affected_areas):
    most_affected = ""
    times_hit = 0
    for area in affected_areas:
        count = affected_areas[area]
        if count > times_hit:
            times_hit = count
            most_affected = area
    return most_affected, times_hit


most_area, hits = find_most_affected_area(affected_areas)
print("Most affected area:", most_area)
print("Number of times hit:", hits)


# 6 Calculating the Deadliest Hurricane to find highest mortality hurricane and the number of deaths
def find_most_deaths(hurricanes):
    deadliest_hurricane = ""
    max_deaths = 0
    for name in hurricanes:
        deaths = hurricanes[name]["Deaths"]
        if deaths > max_deaths:
            max_deaths = deaths
            deadliest_hurricane = name
    return deadliest_hurricane, max_deaths


hurricane_name, deaths = find_most_deaths(Cuba_I)
print("Deadliest hurricane:", hurricane_name)
print("Number of deaths:", deaths)

# 7 Rating Hurricanes by Mortality to categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000}

def categorize_hurricanes_by_mortality(hurricanes):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in hurricanes:
        deaths = hurricanes[name]["Deaths"]
        if deaths == 0:
            rating = 0
        elif deaths <= mortality_scale[1]:
            rating = 1
        elif deaths <= mortality_scale[2]:
            rating = 2
        elif deaths <= mortality_scale[3]:
            rating = 3
        elif deaths <= mortality_scale[4]:
            rating = 4
        else:
            rating = 5
        hurricanes_by_mortality[rating].append(hurricanes[name])
    return hurricanes_by_mortality


hurricanes_by_mortality = categorize_hurricanes_by_mortality(Cuba_I)
print(hurricanes_by_mortality)


# 8 Calculating Hurricane Maximum Damage to find highest damage inducing hurricane and its total cost
def find_most_damage(hurricanes):
    most_damage_hurricane = ""
    max_damage = 0
    for name in hurricanes:
        damage = hurricanes[name]["Damage"]
        if damage == "Damages not recorded":
            continue
        if damage > max_damage:
            max_damage = damage
            most_damage_hurricane = name
    return most_damage_hurricane, max_damage


hurricane_name, damage = find_most_damage(Cuba_I)
print("Hurricane with greatest damage:", hurricane_name)
print("Total damage cost:", damage)

# 9 Rating Hurricanes by Damage
damage_scale = {
    0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000
}


def categorize_hurricanes_by_damage(hurricanes):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in hurricanes:
        damage = hurricanes[name]["Damage"]
        if damage == "Damages not recorded":
            continue
        if damage == 0:
            rating = 0
        elif damage <= damage_scale[1]:
            rating = 1
        elif damage <= damage_scale[2]:
            rating = 2
        elif damage <= damage_scale[3]:
            rating = 3
        elif damage <= damage_scale[4]:
            rating = 4
        else:
            rating = 5
        hurricanes_by_damage[rating].append(hurricanes[name])
    return hurricanes_by_damage


hurricanes_by_damage = categorize_hurricanes_by_damage(Cuba_I)
print(hurricanes_by_damage)