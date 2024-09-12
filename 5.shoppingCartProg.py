#Shopping Cart

item = input("what items would u like to buy?: ")
price = float(input("What is the price?: "))
quantity  = int(input("How many would u like?: "))
total = price * quantity

print(f"you have brought {quantity} x {item}/s")
print(f"yor total is: ${total}")


