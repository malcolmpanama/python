import pyinputplus as pyp

# price of all ingredients
prices = {'wheat': 2, 'white': 1, 'sour dough': 3, 'chicken': 2, 'turkey': 3, 'ham': 2, 'tofu': 1,
          'cheddar': 1, 'swiss': 2, 'mozzarella': 3, 'mayo': 1, 'mustard': 1, 'lettuce': 1,
          'ketchup': 1}

while True:
    ingredients = []
    # options to select bread, protein, cheese with inputMenu() method
    ingredients.append(pyp.inputMenu(['wheat', 'white', 'sour dough'],
                          prompt='Please select the type of bread you want for your sandwich: \n',
                          numbered=True))

    ingredients.append(pyp.inputMenu(['chicken', 'Turkey', 'Ham', 'tofu'],
                            prompt='Which type of protein you would like: \n',
                            numbered=True))

    if pyp.inputYesNo('Do you want Cheese in your sandwich?(Y/N)\n')== 'yes':
        ingredients.append(pyp.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))

    # using inputYesNo() for single ingredients with no further types
    if pyp.inputYesNo('Do you want mayo?(Y/N) \n') == 'yes':
        ingredients.append('mayo')
    if pyp.inputYesNo('Do you want mustard?(Y/N) \n') == 'yes':
        ingredients.append('mustard')
    if pyp.inputYesNo('Do you want lettuce?(Y/N) \n') == 'yes':
        ingredients.append('lettuce')
    if pyp.inputYesNo('Do you want tomato ketchup?(Y/N) \n') == 'yes':
        ingredients.append('ketchup')

    # using inputInt() and blockRegexes that do not allow negative integer, float or 0
    sandwichQT = pyp.inputInt('How much sandwiches you would like to order?\n',
                              blockRegexes=['[0|-|.]'])

    total_amount = 0
    # using for loop to print items, prices and adding their amount to total_amount variable
    print(f'Your sandwich ingredients and prices are as follows: \n')
    for item in ingredients:
        price = prices[item]
        print(f'{item}= {price}')
        total_amount += price

    # at the end printing total amount and how much sandwiches have been ordered
    print(f"sandwich cost x sandwich Qt ordered = {total_amount}x{sandwichQT} = "
          f"{total_amount*sandwichQT}")

    # confirming if the user need to reorder or user wants to confirm the order by simple yes/no
    # if user confirm by typing yes or y then menu will become false and while loop will terminate
    if pyp.inputYesNo('Please confirm your order: (Y/N)\n')== 'yes':
        print('Please take your order number from the machine and you will be notified when '
              'its ready')
        break
