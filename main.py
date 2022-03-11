n = int(input("Enter the number of users: "))
users = []

for i in range(n):
    user = {
        "name": input("Name: "),
        "age" : int(input("Age: "))
    }
    users.append(user)

search = input("Enter a name for search in users: ")

for user in users:
    if user["name"].lower() == search.lower():
        search = ""
        print(user["age"])
        break
    
if search != "":
    print("Not Found")