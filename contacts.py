contacts = {"Ana": ["06 11 22 33 44", "ana@mail.com"]}
name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
contacts[name] = [phone, email]
search = input("Search: ")
if search in contacts:
    phone, email = contacts[search]
    print(f"{search}: {phone} / {email}")
else:
    print(search, "not found")
print(len(contacts), "contacts")