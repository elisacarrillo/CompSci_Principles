#Write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
#Write a program to randomly print a integer number between 7 and 15 inclusive
#Write a program to print the running time of execution of "1+1" for 100 times.

#Problem One
import random
d = []

for x in range(10):
    if x%2 == 0:
        d.append(random.randint(100,200))
print(d)
    
#Problem Two
h = random.randint(7,15)
print(h)

#Problem Three
import time
start = time.time()
x = 0
while x<100:
    print(1+1)
    x = x+1
end = time.time()
print(end-start)
