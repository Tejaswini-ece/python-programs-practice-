# Shopping Cart Program
foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food)

for price in prices:
    total += price

print(f"\nYour total is: ${total:.2f}")
