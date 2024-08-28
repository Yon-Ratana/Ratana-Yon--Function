# EX10.Show product name that has maximum price

def sum(products): 
    max = 0
    name = ''
    for i in range(len(products)):  
        if max==0:
            max=products[0]["price"]
            name=products[i]["name"]
        elif products[i]["price"]>max:
            max==products[i]["price"]
            name=products[i]["name"]
            
    return name
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum(products))