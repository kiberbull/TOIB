import random
 
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
length = input("Число символов в пароле? ")
lenght = int
if lenght < 8:
    lenght = 8
b = int(input("Число паролей? "))
count = 0
passlist = []
while count < b:
    while True:
        password = ''.join(random.choice(symbols) for i in range(a))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    count += 1
    passlist.append(password)
print(passlist)
