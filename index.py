file = open('Food_Database.txt', 'r')
content = file.read()

def add_or_ask():
    user_choice = input("Would you like to add ingredient to database (Add) or look for food? (Look)? ")
    if user_choice.lower() == "look":
        food_choice()
    elif user_choice.lower() == "add":
        add_food()
    else:
        print("It's not a option")
        add_or_ask()
    
def food_choice():
    user_ingredients = input("Ingredients: ")
    with open('Food_Database.txt', 'r') as content_food:
        for ingredients in content_food:
            if user_ingredients in ingredients:
                print(f"\n {ingredients}")
    
    
def add_food():
    print("---------------")
    print("Please answer on this format: Food Name - Ingredient1, Ingredient2")
    user_add = input("")
    with open("Food_Database.txt", "a") as f:     
        f.write(user_add + "\n")
    print(f"The list is updated")
    
add_or_ask()