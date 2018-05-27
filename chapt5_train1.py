def display_inventory(inventory):
    print("Inventry list:")
    item_total = 0
    for k in inventory.keys():
        item_total = item_total + inventory[k]
        print(str(inventory[k]) + " : " + k)
    print("Total amount of items: " + str(item_total))

inventory = {"torch":6, "gold":42, "bow":32, "shuriken":23}

display_inventory(inventory)
