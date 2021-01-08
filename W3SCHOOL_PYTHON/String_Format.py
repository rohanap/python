age = 36
txt = "My name is John,I am " 
print(f"{txt}{age}")

quantity = 3
item = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity,item,price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myOrder.format(quantity,item,price))