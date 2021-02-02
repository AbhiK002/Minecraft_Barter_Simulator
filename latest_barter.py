import random
import keyboard
poss_items = {
    "Water Bottle": 10,
    "Ender Pearl": 10,
    "Iron Nugget": 10,
    "String": 20,
    "Nether Quartz": 20,
    "Crying Obsidian": 40,
    "Fire Charge": 40,
    "Obsidian": 40,
    "Leather": 40,
    "Nether Brick": 40,
    "Soul Sand": 40,
    "Spectral Arrow": 40,
    "Blackstone": 40,
    "Gravel": 40,
    "Enchanted Book (Soul Speed)": 5,
    "Iron Boots (Soul Speed)": 8,
    "Potion (Fire Resistance)": 8,
    "Splash Potion (Fire Resistance)": 8
}  # 459 total


def dict_to_list(raw_dict):
    conv_list = []
    for item, recur in raw_dict.items():
        for i in range(recur):
            conv_list.append(item)
    return conv_list


def n_throws():
    while True:
        throws = input('\nNumber of Gold Ingot Throws: ')
        if throws.isdecimal():
            break
        else:
            print("Please enter a number only\n")
    return throws


def display_inventory():
    print("Inventory:\n")
    raw_det_list = []
    for coll_item, coll_count in inventory.items():
        item_perc = (int(coll_count) / throws) * 100
        item_details = f"{str(coll_item).ljust(31)} :   {str(coll_count).ljust(8)} ({str(round(item_perc, 3))}%)"
        raw_det_list.append(item_details)
    raw_det_list.sort()
    item_detail_output = '\n'.join(raw_det_list)
    print(item_detail_output)


print("~ 1.16.2+ Bartering Simulator ~")
keyboard.add_hotkey('esc', lambda: exit())
poss_items_list = dict_to_list(poss_items)
while True:
    inventory = {}
    throws = int(n_throws())
    print()
    for throw in range(throws):
        barter_rec = random.choice(poss_items_list)
        # print(barter_rec)
        inventory.setdefault(barter_rec, 0)
        if barter_rec in inventory:
            inventory[barter_rec] += 1
    # print('\n'+str(inventory)+'\n')
    inventory.items()
    display_inventory()
