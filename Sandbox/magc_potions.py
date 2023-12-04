"""
Potion buying method
"""
POTIONS = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], 
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] 
}

def print_potions():
    """
    This function prints the names of all available potions.
    
    It iterates over the keys in the POTIONS dictionary (which represent potion names) 
    and prints each one.
    """
    print('Available Potions: ')
    for potion in POTIONS:
        print(potion)

def buy_ingredients(choice):
    """
    This function handles the purchasing of ingredients for a chosen potion.
    
    It first checks if the chosen potion exists in the POTIONS dictionary.
    If the potion does not exist, it prints a message and returns.
    
    If the potion exists, it prints the ingredients for the potion.
    Then it iterates over the ingredients, asking the user if they want to buy each one.
    If the user chooses to buy an ingredient, it prints a confirmation message.
    If the user chooses not to buy an ingredient, it prints a message and returns False.
    
    If the user chooses to buy all ingredients, the function returns True.
    
    Parameters:
    choice (str): The name of the potion the user wants to buy ingredients for.
    
    Returns:
    bool: True if the user chooses to buy all ingredients, False otherwise.
    """
    ingredients = POTIONS.get(choice)
    if ingredients is None:
        print(f"No such potion: {choice}")
        return

    print(f'\nThe ingredients for the {choice} are: ')
    for ingredient in ingredients:
        print(ingredient)

    for ingredient in ingredients:
        buy_ingredient = input(f'Would you like to buy {ingredient}? (Y/N): ')
        if buy_ingredient.upper() == 'Y':
            print(f"You bought {ingredient}")
        else:
            print(f"You didn't buy {ingredient}")
            return False
    return True

def main():
    """
    This is the main function that controls the flow of the program.
    It repeatedly asks the user which potion they would like to buy ingredients for,
    calls the buy_ingredients function to handle the purchase,
    and asks the user if they would like to continue shopping.
    """
    still_shopping = True
    while still_shopping:
        print_potions()
        choice = input('Which potion would you like to buy ingredients for? ').title()
        all_purchased = buy_ingredients(choice)
        if all_purchased:
            print("You bought all ingredients!")
        still_shopping = input('Would you like to continue shopping? (Y/N): ').upper() == 'Y'

if __name__ == "__main__":
    main()