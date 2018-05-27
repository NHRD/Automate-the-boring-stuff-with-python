def add_to_inventory(inventory, added_item):
    for i in added_item:
        if i not in inventory:
            inventory.setdefault(i, 1)
        else:
            inventory[i] = int(inventory[i]) + 1
    return inventory

def display_inventory(inventory):
    print("Inventry list:")
    item_total = 0
    for k in inventory.keys():
        item_total = item_total + inventory[k]
        print(str(inventory[k]) + " : " + k)
    print("Total amount of items: " + str(item_total))

inventory = {"torch":6, "gold":42, "bow":32, "shuriken":23}
dragon_loot = ["torch", "gold", "bow", "shuriken", "ruby" , "bow", "shuriken", "ruby" ]

display_inventory(add_to_inventory(inventory, dragon_loot))