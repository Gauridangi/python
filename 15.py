print("Welcome to the Guest list Manager")
print("You can perform up to 5 action")
print("Add a guest to the list.")
print("View the current list of guests.")
print("Remove a guest by their name.")
print("exist the program.")
mylist = []
for x in range(5):
    guestlist = input("Enter the guest name:")
    mylist.append(guestlist)
print(mylist)
guestremove = input("Do you want remove any guest").lower()
if guestremove == "yes":
    remove = input("Enter move guest")
    mylist.remove(remove)
    print(mylist)
else:
    print(mylist)
    