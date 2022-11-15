import random
import time

uppercase= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
Symbols = "!@#$%^&*(){}[];'/.,:\"?><"
the_password=''
ASCIIall= uppercase+lowercase+numbers+Symbols

syste = "Hello, I am the password generator, The more charachters, the harder the password"

for i in syste:
    print (i, end='') #To Use the same line
    time.sleep(.05)
    

passlong = input("\nHow many charachters you would like? : ")

numb = int(passlong)

for i in range(numb):
    the_password=the_password+random.choice(ASCIIall)

print (the_password)
    
    



