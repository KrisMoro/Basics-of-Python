"""Task 1 and 2 in module 2."""


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby', 
    'rubbish', 'chewed gum', 'used tissue']

def display_inventory(inventory):
    """Display current inventory."""
    print("Inventory:")
    item_total = 0
    overload_warning =''
    for item_name, item_count in inventory.items():
        item_total += item_count
        print(str(item_count) + ' ' + item_name)
    print("\nTotal number of items: " + str(item_total)+'\n')
    if item_total >= 60 and item_total < 70:
        overload_warning = 'CAUTION: Your backpack weighs a lot, your stamina runs out quicker!\n'
    elif item_total >= 70 and item_total < 80:
        overload_warning = 'CAUTION: Your equipment is very heavy, you\'re moving slower than usual!\n' 
    elif item_total >=80:
        overload_warning = 'CAUTION: You are overloaded, can\'t move!\n'
    print(overload_warning)


def add_to_inventory(inventory, added_items):
    """Add new items to inventory."""
    trash = ('rubbish', 'chewed gum', 'used tissue')
    for item_name in added_items:
        if item_name not in trash:
            if item_name in inventory:
                inventory[item_name] += 1
            else:
                inventory[item_name] = 1
    return inventory


display_inventory(stuff)
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
