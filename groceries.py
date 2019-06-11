# groceries.py

#from pprint import pprint
from operator import itemgetter

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


# TODO: write some Python code here to accomplish basic task
products_count = len(products)

# header
print("----------------")
print(f"THESE ARE THE {products_count} PRODUCTS:")
print("----------------")

##################################################OLD LOGIC##################################################
# product_price = []
# appending formatted elements in product_price list
#for index in range(len(products)):
#    product_price.append(products[index]["name"] + " (" + "$" + str(products[index]["price"]) + ")")
#
#
# sort and print the elements of product_price list
#product_price.sort()
#for i in range(len(product_price)):
#    print("+ " + product_price[i])
#
    #print(products[index]["name"] + " (" + "$" + str(products[index]["price"]) + ")")

#################################################################################################################

# sorting a list of dictionaries
products_sorted = sorted(products, key = itemgetter('name'))
# print(products_sorted)

#print each product iteration
for item in products:
    item_price = "${0:,.2f}".format(item['price'])
    #print(f"+ {item['name']} ({item['price']})")
    print(f"+ {item['name']} ({item_price})")

# TODO: write python code to accomplish challenge task

print("\n")    # empty space

# Get a list of distinct departments, sorted in ascending order

department_set = set()

for item in products:
    department_set.add(item['department'])

department_list = list(department_set)
#print(department_list)


# distinct department count
dept_count = len(department_list)

# header
print("----------------")
print(f"THESE ARE THE {dept_count} PRODUCTS:")
print("----------------")

#print each department iteration
for dept in department_list:
    product_count = len([i["name"] for i in products if i["department"] in dept])
    if product_count == 1:
        p_string =  "Product"
    else:
        p_string = "Products"

    print(f"+ {dept} ({product_count} {p_string})")
    
    



# p for p in products if p["departments"] == "snacks"