# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages(damages, conversion):
  damages_list=[]
  for damage in damages:
    if "M" in damage:
      damage=damage.strip("M")
      damage=float(damage)
      damage*=conversion["M"]
    elif "B" in damage:
      damage=damage.strip("B")
      damage=float(damage)
      damage*=conversion["B"]
    else:
      damage="Damages not recorded"
    damages_list.append(damage)
  return damages_list
# test function by updating damages
updated_damages=convert_damages(damages, conversion)


# 2
def dict_creator(names, months, years, max_sustained_winds, areas_affected, updated_damages,deaths):
  hurricanes={}
  data_number=len(names)
  for i in range(data_number):
   hurricanes[names[i]]={"Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Deaths": deaths[i]}
  return hurricanes

hurricanes=dict_creator(names, months, years, max_sustained_winds, areas_affected, updated_damages,deaths)

# 3
# Organizing by Year
def year_organizer(hurricanes):
  hurricanes_by_year={}
  for hurricane in hurricanes:
    hurricane_year=hurricanes[hurricane]["Year"]
    current_hurricane=hurricanes[hurricane]
    if hurricane_year not in hurricanes_by_year:
      hurricanes_by_year[hurricane_year]=[current_hurricane]
    else:
      hurricanes_by_year[hurricane_year].append(current_hurricane)
  return hurricanes_by_year

hurricanes_by_year=year_organizer(hurricanes)

# 4
# Counting Damaged Areas
def area_counter(hurricanes):
  area_incidence={}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]["Areas Affected"]:
      area_count=1
      if area not in area_incidence:
        area_incidence[area]=1
      else:
        area_incidence[area]+=1
  return area_incidence

area_count=area_counter(hurricanes)

# 5
# Calculating Maximum Hurricane Count
def most_affected_finder(area_count):
  most_affected=None
  max_count=0
  for key, value in area_count.items():
    if value>max_count:
      max_count=value
      most_affected=key
  return most_affected, max_count

most_affected_area= most_affected_finder(area_count)

# 6
# Calculating the Deadliest Hurricane
def deadliest_finder(hurricanes):
  deadliest=None
  deaths=0
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"]>deaths:
      deaths=hurricanes[hurricane]["Deaths"]
      deadliest=hurricanes[hurricane]["Name"]
  return deadliest, deaths

deadliest_hurricane=deadliest_finder(hurricanes)

# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_rating={0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hurricane in hurricanes:
    rating=None
    deaths=hurricanes[hurricane]["Deaths"]
    if deaths == mortality_scale[0]:
      hurricanes_by_rating[0].append(hurricanes[hurricane])
    elif deaths>mortality_scale[0] and deaths<=mortality_scale[1]:
      hurricanes_by_rating[1].append(hurricanes[hurricane])
    elif deaths>mortality_scale[1] and deaths<=mortality_scale[2]:
      hurricanes_by_rating[2].append(hurricanes[hurricane])
    elif deaths>mortality_scale[2] and deaths<=mortality_scale[3]:
      hurricanes_by_rating[3].append(hurricanes[hurricane])
    elif deaths>mortality_scale[3] and deaths<=mortality_scale[4]:
      hurricanes_by_rating[4].append(hurricanes[hurricane])
    elif deaths>mortality_scale[4]:
      hurricanes_by_rating[5].append(hurricanes[hurricane])
  return hurricanes_by_rating

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality=categorize_by_mortality(hurricanes)


# 8 Calculating Hurricane Maximum Damage
def calculate_greatest_damage(hurricanes):
  most_damage=None
  max_cost=0
  for hurricane in hurricanes:
    cost=hurricanes[hurricane]["Damage"]
    if cost == "Damages not recorded":
      pass
    elif cost>max_cost:
      max_cost=cost
      most_damage=hurricanes[hurricane]["Name"]
  return most_damage, max_cost
# find highest damage inducing hurricane and its total cost
greatest_damage_hurricane=calculate_greatest_damage(hurricanes)

# 9
# Rating Hurricanes by Damage
def categorize_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage={0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hurricane in hurricanes:
    rating=None
    damage=hurricanes[hurricane]["Damage"]
    if damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[hurricane])
    elif damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[hurricane])
    elif damage>damage_scale[0] and damage<=damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[hurricane])
    elif damage>damage_scale[1] and damage<=damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[hurricane])
    elif damage>damage_scale[2] and damage<=damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[hurricane])
    elif damage>damage_scale[3] and damage<=damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[hurricane])
    elif damage>damage_scale[4]:
       hurricanes_by_damage[5].append(hurricanes[hurricane])
  return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage=categorize_by_damage(hurricanes)
print(hurricanes_by_damage[5])
