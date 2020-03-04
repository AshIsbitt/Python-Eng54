dict = {'key': 'value', 'text':'entry'}

boris_disct = {
    'name':'boris',
    'l_name':'Johnson',
    'phone':'07952342343',
    'address':'10 Downing st'
}

# access KV pair
print(boris_disct['l_name'])

# change the value

boris_disct['phone'] = "+7 19239429"

# assign new KV pair
boris_disct['home_phone'] = "+44 01851943"

boris_disct['budgets_passed'] = 0
print(boris_disct['budgets_passed'])
boris_disct['budgets_passed'] += 1
print(boris_disct['budgets_passed'])

# get all keys
print(boris_disct.keys())

# get all valies
print(boris_disct.values())

# nested structures
