import sys


class Mobiephone:
    def __init__(self):
        self.mobilenames = ["Samsung S20FE", "Samsung M51", "Samsung A51"]
        self.RAM = ["8", "6/8", "4/6/8"]
        self.ROM = ["128", "128", "64/128"]
        self.proce = ["Exy990", "Sd730G", "Exy9611"]
        self.battery = [4500, 7000, 4000]
        self.disp = [6.4, 6.7, 6.5]

    def displayAvailablemobiles(self):
        print("")
        print("The mobiles we have in our library are as follows:")
        cnt = 1
        for mobile in self.mobilenames:
            print(cnt, ". ", mobile)
            cnt += 1
        print("")
        print("""Want to view specifications of a mobile?
        1. Yes
        2. No""")
        ch = int(input("Enter Choice: "))
        if(ch == 1):
            cho = int(input("Select the Mobile from list above: "))
            if(cho > 3):
                print("\nInvalid Input. If requested to add a Mobile's",
                      "Specification. Please give us some time to add")
            else:
                print("")
                print("Mobile Name - ", self.mobilenames[cho-1],
                      "\nRAM \t\t- ", self.RAM[cho-1], "GB\nROM \t\t- ",
                      self.ROM[cho-1], "GB\nProcessor \t- ", self.proce[cho-1],
                      "\nBattery \t- ", self.battery[cho-1],
                      "mAh\nDisplay \t- ", self.disp[cho-1], "inches")
        elif(ch == 2):
            pass
        else:
            print("\nInvalid Input")

    def add1mobile(self):
        mobilename = input("Enter the name of the mobile you want to request:")
        self.mobilenames.append(mobilename)
        print("Thanks for adding Mobile name")


def main():
    mp = Mobiephone()
    while 1:
        print("""
              ======Mobile Phone Guide by Akshay Sai Reddy G=======
              1. Display all mobiles list
              2. Request Admin to add a Mobile's Specification
              0. Exit""")
        choice = int(input("Enter Choice:"))
        if choice == 1:
            mp.displayAvailablemobiles()
        elif choice == 2:
            mp.add1mobile()
        elif choice == 0:
            sys.exit()
        else:
            print("Invalid Input. Please select from below options.")

main()
