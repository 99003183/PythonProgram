import sys
import re


class Mobiledata:
    def __init__(self):
        self.mobilename = ["Samsung S20FE", "Samsung M51", "Samsung A51"]
        self.RAM = ["8", "6/8", "4/6/8"]
        self.ROM = ["128", "128", "64/128"]
        self.proce = ["Exy990", "Sd730G", "Exy9611"]
        self.battery = [4500, 7000, 4000]
        self.disp = [6.4, 6.7, 6.5]


class Mobileinfo(Mobiledata):
    def displayAvailablemobiles(self):
        print("")
        print("The mobiles we have in our library are as follows:")
        cnt = 1
        for mobile in self.mobilename:
            print(cnt, ". ", mobile)
            cnt += 1
        print("")
        print("""Want to view specifications of a mobile?
        1. Yes
        2. No""")
        ch = int(input("Enter Choice: "))
        if(ch == 1):
            print("Enter the Serial No. of Mobile from list above: ")
            cho = int(input())
            if(cho > 3):
                print("\nInvalid Input. If requested to add a Mobile's",
                      "Specification. Please give us some time to add")
            else:
                print("")
                print("Mobile Name - ", self.mobilename[cho-1],
                      "\nRAM \t\t- ", self.RAM[cho-1], "GB\nROM \t\t- ",
                      self.ROM[cho-1], "GB\nProcessor \t- ", self.proce[cho-1],
                      "\nBattery \t- ", self.battery[cho-1],
                      "mAh\nDisplay \t- ", self.disp[cho-1], "inches")
        elif(ch == 2):
            pass
        else:
            print("\nInvalid Input")


class mobileadd(Mobiledata):
    def add1mobile(self):
        mobilenam = input("Enter the name of the mobile you want to request: ")
        self.mobilename.append(mobilenam)
        print("\nThanks for requesting this Mobile. Please give us some time",
              "to add it.\n\n")


def main():
    mp = Mobileinfo()
    mp1 = mobileadd()
    while 1:
        print("""
              ======Mobile Phone Guide by Akshay Sai Reddy G=======
              1. Display all mobiles list
              2. Request Admin to add a Mobile's Specification
              3. View Patter Matching(using Regular Expression)
              0. Exit""")
        choice = int(input("Enter Choice number:"))
        if choice == 1:
            mp.displayAvailablemobiles()
        elif choice == 2:
            mp1.add1mobile()
        elif choice == 3:
            print("\nPattern Matching for \'akshaysai@gmail.com' is:")
            print(re.match("[a-z]+@[a-z]+.[a-z]+", "akshaysai@gmail.com"))
        elif choice == 0:
            sys.exit()
        else:
            print("Invalid Input. Please select from below options.")

main()
