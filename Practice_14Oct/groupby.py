import itertools

l1 = [
    {
    'city':'Bangalore',
    'state':'karnataka'
    },
    {'city':'Chennai',
     'state':'Tamilnadu'
    },
    {'city':'Chennai',
     'state':'Tamilnadu'
    },
    {'city':'Bangalore',
     'state':'karnataka'
    },
    {'city':'Chennai',
     'state':'Tamilnadu'
    }
]

output= itertools.groupby(l1,key=lambda x:x['city'])
#print(list(output))

for key,group in output:
    print(key)
    for a in group:
        print(a)


import itertools

# def return_state(people):
#     return people['state']
#
# people = [
#     {
#         'name': 'John Doe',
#         'city': 'Gotham',
#         'state': 'NY'
#     },
#     {
#         'name': 'Jane Doe',
#         'city': 'Kings Landing',
#         'state': 'NY'
#     },
#     {
#         'name': 'Corey Schafer',
#         'city': 'Boulder',
#         'state': 'CO'
#     },
#     {
#         'name': 'Al Einstein',
#         'city': 'Denver',
#         'state': 'CO'
#     },
#     {
#         'name': 'John Henry',
#         'city': 'Hinton',
#         'state': 'WV'
#     },
#     {
#         'name': 'Randy Moss',
#         'city': 'Rand',
#         'state': 'WV'
#     },
#     {
#         'name': 'Nicole K',
#         'city': 'Asheville',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jim Doe',
#         'city': 'Charlotte',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jane Taylor',
#         'city': 'Faketown',
#         'state': 'NC'
#     }
# ]
#
# output = itertools.groupby(people,lambda x : x['state'])
#
# for state,peopledata in output:
#     print(state)
#     for a in peopledata:
#         print(a)
#
