import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lol = int(input("ingrese la longitud de la contraseña"))
password = ""
for i in range(lol):
    password += random.choice(caracteres)

print("su contraseña es",password)