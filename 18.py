print("Welcome to the resturant")
menu = {
    "burger":270,
    "pizza":350,
    "momo":120,
    "chaumin":100,
    "chicken chilly":350
}
orderlist = []
totalamount = 0
for x in menu:
    print(f"{x} {menu[x]}")
print("Enter a dish you want")
for x in range(5):
    order = input("Dish: ")
    if order == "done":
        break
    elif order in menu:
        orderlist.append(order)
        totalamount += menu[order]
        print(f"{order} added to order. price Rs.{menu[order]}")
    else:
        print("sorry, we don't serve")
