menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("------------MENU----------------")

for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("--------------------------------")    

while True:
    food = input("Select an item (q to quit): ").lower()
    
    # Quit the loop if user inputs 'q'
    if food == "q":
        break

    # Check if food item exists in the menu
    elif menu.get(food) is not None:
        cart.append(food)  # Add valid food item to the cart
    
    # Handle case when food is not in the menu
    else:
        print(f"Sorry, {food} is not on the menu. Please choose a valid item.")

# Calculate and print the total cost and items in the cart
print("\nItems in your cart:")
for food in cart:
    price = menu.get(food)
    
    # Ensure the item has a valid price
    if price is not None:
        total += price
        print(f"{food} - ${price:.2f}")

# Print the total cost
print(f"\nTotal cost: ${total:.2f}")
