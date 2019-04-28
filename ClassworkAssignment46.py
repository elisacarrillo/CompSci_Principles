#Write a program to shuffle and print the list [3,6,7,8]
import random
d = [3,6,7,8]
for x in range(1):
    print(random.choice(d))

#Write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
import time
start = time.time()
subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey", "Football"]

car = [[s,v,o] for s in subject for v in verb for o in objects]
print(car)
end = time.time()
print(end - start)


    
#Generate a Random number between 2 and 5000

for x in range(1):
    print(random.randint(2,5000))
