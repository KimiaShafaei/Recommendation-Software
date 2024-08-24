from node import Node
from LinkedList import LinkedList
from restaurantData import types, restaurant_data

def food_type():
    food_type_lst = LinkedList()
    for type in types:
        food_type_lst.add_to_end(type)
    return food_type_lst


def restaurant_details():
    details_lst = LinkedList()
    for detail in restaurant_data:
        category, name, food_quality, service_quality, address = detail
        restaurant_info = {"Category": category, "Name": name, "Food quality": food_quality, "Service quality": service_quality, "Address": address}
        details_lst.add_to_end(restaurant_info)
    return details_lst

def choose_food_type(user, food_type_lst):
    current = food_type_lst.head
    suggest = []
    while current:
        if current.value.startswith(user.lower()):
            suggest.append(current.value)
        current = current.next
    return suggest

def recommend_restaurant(selected, restaurant_info_lst):
    current = restaurant_info_lst.head
    recommend = []
    while current:
        if selected.lower() == current.value["Category"]:
            recommend.append(current.value)
        current = current.next
    return recommend

food_types = food_type()
restaurant_info = restaurant_details()

user_input = input("What type of food would yo like to eat?\n Type the beginnig of that food type: ")
suggestions = choose_food_type(user_input, food_types)
if suggestions:
    print("With those beginning letters your choices are: ")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}) {suggestion}")
    
    select = int(input("Select your food type: ").lower())
    selected = suggestions[select - 1]
    recommendations = recommend_restaurant(selected, restaurant_info)
    if recommendations:
        print(f"Here are some {selected} restaurant:")
        for recommendation in recommendations:
            print(f"""{recommendation["Name"]}\nFood quality: {recommendation["Food quality"]}\nService quality: {recommendation["Service quality"]}\nAddress: {recommendation["Address"]}\n-------------------""")
    else:
        print("No restaurant found")
else:
    print("No options")