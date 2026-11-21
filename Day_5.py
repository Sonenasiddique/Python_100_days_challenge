# Generating  a  Strong password program
import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = ['0','1','2','4','6','7','3']
Symbols = ['@','$','&','#','*','!']

print("Welcom to Password Generator!")
letter_no =  int(input("How many letter do you want in your password ?"))
number_no = int(input("How many number do you want ?"))
symbol_no = int(input("How many symbols do you want ?"))

password = []

for letter in  range(letter_no):
    letter_cho = random.choice(Letters)
    password.append(letter_cho)

for number in range(number_no):
        number_cho = random.choice(Numbers)
        password.append(number_cho)
        
for symbol in range(symbol_no):
           symbol_cho = random.choice(Symbols)
           password.append(symbol_cho)

result ="".join(password)
print(f"The Password is {result}")

