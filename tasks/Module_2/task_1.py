stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    overload_warning =''
    for item_name, item_count in inventory.items():
        item_total += item_count
        print(str(item_count) + ' ' + item_name)
    print("\nTotal number of items: " + str(item_total)+'\n')
    if item_total >= 60 and item_total < 70:
        overload_warning = 'CAUTION: Your backpack weighs a lot, your stamina runs out quicker!'
    elif item_total >= 70 and item_total < 80:
        overload_warning = 'CAUTION: Your equipment is very heavy, you\'re moving slower than usual!' 
    elif item_total >=80:
        overload_warning = 'CAUTION: You are overloaded, can\'t move!'
    print(overload_warning)
display_inventory(stuff)
