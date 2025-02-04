copyright["silver productions"]

name = input("username[#] ")
password = input("password[%] ")
email = input("contacts[@] ")

name_encoding = [ord(char) for char in name]
password_encoding = [ord(char) for char in password]
email_encoding = [ord(char) for char in email]

print("\n" + "name: " + name)
print("password: " + password)
print("contacts: " + email + "\n")

print(name_encoding)
print(password_encoding)
print(email_encoding)
print(" ")

while True:
    input()
