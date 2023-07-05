def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f'{num}. {dwarf}')
        num+=1


def summon_captain_planet(elements):
    return [f'{element.capitalize()}!' for element in elements ]
    

def long_planeteer_calls(calls):
    return any([call for call in calls if len(call)>4])
    

def find_the_cheese(foods):
    types_of_cheese = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in types_of_cheese: 
            return food
    return None

soup = ["tomato soup", "oyster crackers"]
print(find_the_cheese(soup))