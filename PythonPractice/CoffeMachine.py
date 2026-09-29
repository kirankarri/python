
coffee_variant_requirement = {
    'espresso':{
        'Water': 50,
        'Coffee': 18,
        'Milk': 0,
        'Cost': 1.5
    },
    'latte':{
        'Water': 200,
        'Coffee': 24,
        'Milk': 150,
        'Cost': 2.5,
    },
    'cappuccino':{
        'Water': 250,
        'Coffee': 24,
        'Milk': 100,
        'Cost': 3.0
    }
}

Available_Resources = {
    'Water': 300,
    'Coffee': 100,
    'Milk': 200,
    'Cost': 0

}

def drink_requirements(coffee_variant):
    ###This function is to 
    ###
    if (coffee_variant_requirement[coffee_variant]['Water'] <= Available_Resources ['Water'] and
        coffee_variant_requirement[coffee_variant]['Coffee'] <= Available_Resources ['Coffee'] and
        coffee_variant_requirement[coffee_variant]['Milk'] <= Available_Resources ['Milk']):
        return True
    return False

def coffee_Price_check(coffe_variant):
    Selected_variant_Cost = coffee_variant_requirement[coffee_variant]['Cost']
    print(f'This coffee costs {Selected_variant_Cost}')
    print('Please insert coins')
    quarters = float(input('How many quarters?'))
    dimes = float(input('How many dimes?'))
    nickles = float(input('How many nickles?'))
    pennies = float(input('How many pennies?'))
    Total_inserted_value = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    if Selected_variant_Cost < Total_inserted_value:
        print(f'Heres your change {round(Total_inserted_value - Selected_variant_Cost,2)}')
        return True
    elif Selected_variant_Cost == Total_inserted_value:
        return True
    else:
        print('Sorry thats not enough money. Money refunded.')
        return False

def Prepare_Coffee(coffee_variant):
    global Available_Resources
    Available_Resources['Water'] -= coffee_variant_requirement[coffee_variant]['Water']
    Available_Resources['Coffee'] -= coffee_variant_requirement[coffee_variant]['Coffee']
    Available_Resources['Milk'] -= coffee_variant_requirement[coffee_variant]['Milk']
    Available_Resources['Cost'] += coffee_variant_requirement[coffee_variant]['Cost']


#Input Cofee Variant
Machine_Running_Status = True
while Machine_Running_Status:
    coffee_variant = input('What would you like today espresso/latte/cappuccino\n')
    if coffee_variant == 'off':
        print('Cofee Machine is shutdown for maintenance')
        Machine_Running_Status = False
    elif coffee_variant == 'report':
        print(Available_Resources)
    elif drink_requirements(coffee_variant):
        if coffee_Price_check(coffee_variant):
            Prepare_Coffee(coffee_variant)
            print(f'Here is your {coffee_variant}. Enjoy!')
    else:
        print('Sorry there is no enough resources')


    


