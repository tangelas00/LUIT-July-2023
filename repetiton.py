import random

number = random.randint(0, 10)

counter = 0
while number != 7:
    if counter >= 14:
        break
    counter = counter + 1 # counter += 1
    number = random.randint(0, 10)
    
print(counter, number)

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
for i in range(40):
    print(i)
