#this function uses a mutable default argument
def addToCart(item,cart=[]):
    cart.append(item)
    return cart

#functions as expected
cart1 = ["apples","milk"]
addToCart("bread",cart1)

#functions as expected
cart2 = addToCart("bread")
addToCart("cheese",cart2)

cart3 = addToCart("oranges")

print(*cart1, sep =', ')

print(*cart2, sep =', ')

print(*cart3, sep =', ')