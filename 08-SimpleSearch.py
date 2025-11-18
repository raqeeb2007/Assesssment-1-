names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

query = input("Input Any Name To Search Through Inventory: ")

if query.capitalize() in names:
    print(f"{query} was found in the inventory.")
else:
    print(f"{query} was not found in the inventory.")   