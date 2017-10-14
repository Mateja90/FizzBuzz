#-*- coding: utf-8 -*-

pozdrav ="Dobrodošli v FIZZBUZZ"
print (pozdrav)
print(pozdrav.lower())

num = raw_input("Prosim vnesi število med 1 in 100: ")

while True:

    if num.isdigit() and int(num) < 100 and int(num) > 0:
        break
    else:
        print("Prosim vnesite število.")
        num = raw_input("Prosim vnesi število med 1 in 100: ")



for i in range(int(num)+1):
    if i == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print ("buzz")
        continue
    else:
        print(str(i))

