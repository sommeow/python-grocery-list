shopping_list = [] 

def show_help(): 
    print("\n****WHAT DO YOU WANT TO PICK UP?****")
    print("""
          Enter 'DONE' to stop adding items
          Enter 'Show' to see your list of items
          """)

def show_list():
    # print out our list function
    print("Here is what you have in your shopping list:")

    for item in shopping_list:
        print(item)

def add_food_to_list(new_item):
    # this function will add new items to the shopping list
    shopping_list.append(new_item)
    print("Added {}. Your shopping list now has {} items(s).".format(new_item, len(shopping_list)))

show_help()

while True:
    # ask for new item
    new_item = input(" > ")
    # able to quit the app
    if new_item == "Done":
        show_list()
        break 
    elif new_item == "Show":
        show_list()
        continue
    add_food_to_list(new_item)