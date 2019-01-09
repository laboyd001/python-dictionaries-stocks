stockDict = { 
    'GM': 'General Motors',
    'CAT':'Caterpillar', 
    'EK':"Eastman Kodak",
    'GE':"General Electric",
     }

purchases = [ 
    ( 'GE', 100, '10-sep-2001', 48 ),
    ('GM', 200, '11-sep-2007', 35),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ('GM', 50, '4-apr-1987', 53),
    ('EK', 450, '37-apr-1987', 13),
    ( 'GE', 200, '1-jul-1998', 56 ) 
    ]

# create a purchase history report that computes full purchase price:
# for stocks in purchases:
#     print("Company name: ", stockDict[stocks[0]], "|| Full purchase price = ", stocks[1]*stocks[3])

# create a second report that accumulates total investment by ticker symbol.  
# purchase_summary = {
#     'GE': [(100, '10-sep-2001', 48), (200, '1-jul-1998', 56)],
#     'CAT': [(100, '1-apr-1999', 24)],
# }

# for purchase in purchase_summary.values():
#     print(purchase[0][0]*purchase[0][2])

# for key, value in purchase_summary.items():
#     print(key, "\n", value) 
#     for purchase in purchase_summary.values():
#        print("\nTotal value in portfolio: ", purchase[0][0]*purchase[0][2])

# Joe's Code ===================================================

# 1 individual out:
# 2 build up a collection we can loop over that contains each company and all the purchases we made of that company's stock:
# report = {
#   'GE': [('GE', 100, '10-sep-2001', 48), ('GE', 200,       '1-jul-1998', 56)],
#     'CAT': [('CAT', 100, '1-apr-1999', 24)],
# }

report = {}
for purchase in purchases:
    abbrev = purchase[0]
    full_name = stockDict[abbrev]
    no_of_shares = purchase[1]
    purch_date = purchase[2]
    purch_price = purchase[3]
    full_purchase_price = no_of_shares * purch_price
    # f below is for .format()
    print(f"I purchased {full_name} stock on {purch_date} for ${full_purchase_price}.")

    try:
        report[abbrev].append(purchase)
    except KeyError:
        report[abbrev] = list()
        report[abbrev].append(purchase)

for abbrev, purchases in report.items():
    print(f"-----{abbrev}----")
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(f"   {purchase}")
    print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")


# Comprehensions ============================================
flowers = ['lily', 'snapdragon', 'rose', 'tulip']
bees = ['bumblebee', 'honeybee', 'dobee', 'aybee']

# reg way:
# flowers_quotes = []
# for flower in flowers:
#     flowers_quotes.append(f"{flower}s make me sneeze")

# comprehension way: (for a list)
flowers_quotes = [f'{flower}s make me sneeze' for flower in flowers]

# comprehension way: (for a set)
# flowers_quotes = {f'{flower}s make me sneeze' for flower in flowers}

# print(flowers_quotes)

# reg nested loop:
# large_flowers = []
# for flower in flowers:
#     for bee in bees:
#         large_flowers.append(f'The {bee} pollinates the {flower}')
# print(large_flowers)

# comprehension way
large_flowers = [
    f'The {bee} pollinates the {flower}' 
    for flower in flowers 
    for bee in bees
    ]

print(large_flowers)

my_family = {
    'sister': {
        'name': 'Sarah',
        'age': 43
    },
    'mother': {
        'name': 'Judy',
        'age': 76
    },
    'father': {
        'name': 'Ray',
        'age': 79
    }
}

# The loop way
# family_stuff = set()
# for family_member, member_values in my_family.items():
#   family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' )


# As a dict comprehension:
family_stuff = {f"{member_values['name']} is my {family_member} and is {str(member_values['age'])} years old" for (family_member, member_values) in my_family.items()}

print(family_stuff)


