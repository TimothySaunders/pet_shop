def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, value):
    pet_shop["admin"]["total_cash"] += value

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, value):
    pet_shop["admin"]["pets_sold"] += value

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)



