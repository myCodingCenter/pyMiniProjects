food = []
price = []
total = 0
while True:
    foodWant = input("Enter food you want to buy(q for quit): ")
    if foodWant == 'q':
        break
    foodWantPrice = input(f"Enter price of {foodWant}: $")
    food.append(foodWant)
    price.append(foodWantPrice)
    food_price = dict(zip(food,price))

print("----YOUR ORDER----")
for i,j in food_price.items():
    print(i+'-----$'+j)
for i in price:
    total = total + float(i)
print(f"your total amount = ${total:.2f}")