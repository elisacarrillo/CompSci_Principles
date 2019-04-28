import os
class Inventory:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def newpart(self):
        f = open('partinventory.txt', 'a')
        write = str(x) + ": " + str(y) + ";\n"
        f.write(write)
        f.close
    
while True:
    try:
        mainmenu = int(raw_input("Would you like to... \n1. View Inventory \n2. Add Part \n3. Remove Part \n4. Take Inventory \n5.Exit and Save\n"))
        if mainmenu == 1:
            with open("partinventory.txt", "r") as ph:
                print("\n")
                read = ph.readlines()
                readstring = "".join(read)
                print(readstring)
            ph.close()
            
        if mainmenu == 2:
            x = raw_input("What is the name of the part you would like to add?\n")
            y = int(raw_input("How many " + x.lower() + "s do you have?\n"))
            part1 = Inventory(x, y)
            part1.newpart()
       
        if mainmenu == 3:
            h = raw_input("\nWhat is the name of the part you would like to remove\n")
            f = open("partinventory.txt", "r").readlines()
            os.remove("./partinventory.txt")  
            with open("partinventory.txt", "w") as k:
                for line in f:
                    
                    if h.lower() not in line:
                        k.write(line)
                    else:
                        print("Removing...")
                            
            
                    
        if mainmenu == 4:
            d = {}
            with open("partinventory.txt") as f:
                k = f.readlines()
                for line in k:
                    (key, val) = line.split()
                    d[(key)] = input("Please input new inventory value for "+ key)
                    

            list_key_values = [[key, val] for key, val in d.items()]
            for x in list_key_values:
                string = ";".join([str(x) for x in list_key_values])
                string1 = string.replace("[", "")
                string2 = string1.replace(",", "")
                string3 = string2.replace("]", "")
                string4 = string3.replace("'", "")
                print(string4)
                with open("partinventory.txt", "w") as h:
                    for word in string4.split(";"):
                        h.write("%s;\n" %word.lower())
                    

        if mainmenu == 5:
            print("Thanks for using Carrillo Industries software :)")
            break
    except:
        print("Please input a valid option!")

