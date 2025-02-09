#Make a discount function

#Base price and discounts
price = 3.14
discount = 0.5

#Prints intital price
print(price)

#Discount method
def calculate_discount(price, discount):
    price *= discount
    return(price)

#Runs the method
price = calculate_discount(price, discount)

#Prints the new price
print(price)
