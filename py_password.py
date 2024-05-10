letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("0: If you don't want any one or two of the following in your password.")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

passwords=[]
password=''

if nr_letters!=0:
    for i in range(0, nr_letters+1):
        passwords.append(random.choice(letters))

if nr_symbols!=0:
    for j in range(0, nr_symbols+1):
        passwords.append(random.choice(symbols))

if nr_numbers!=0:
    for k in range(0, nr_numbers+1):
        passwords.append(random.choice(numbers))

random.shuffle(passwords)

for l in passwords:
    password += l

print(f"Your strong password has been generated!\n\t-->The password is: {password}")
print("\nNote: Some websites or apps don't support certain types of 'symbols' or 'number' or 'alphabet' combinations. So double check your necessity and choose your password accordingly! Therefore, you can eliminate those strings from your final password that is unnecessary!")