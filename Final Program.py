# MOBILE PHONE GUIDE by Akshay Sai Reddy G
import re


# Mobiledata is the parent class containing all the mobile data
class Mobiledata:
    def __init__(self):
        # Below are parameters of the Mobile Phone considered
        self.mobilename = ["Samsung S20FE", "Samsung M51", "Samsung A51",
                           "Realme 5Pro"]
        self.RAM = ["8", "6/8", "4/6/8", "6/8"]
        self.ROM = ["128", "128", "64/128", "64/128"]
        self.proce = ["Exy990", "Sd730G", "Exy9611", "Sd712"]
        self.battery = [4500, 7000, 4000, 4000]
        self.disp = [6.4, 6.7, 6.5, 6.3]


# Mobileinfo is child class which is used to print Data
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
            if(cho > 4):
                print("\nInvalid Input. If requested to add a Mobile's",
                      "Specification. Please give us some time to add")
            else:
                # Printing the deatils of specific mobile
                print("")
                print("Mobile Name - ", self.mobilename[cho-1],
                      "\nRAM \t\t- ", self.RAM[cho-1], "GB\nROM \t\t- ",
                      self.ROM[cho-1], "GB\nProcessor \t- ",
                      self.proce[cho-1], "\nBattery \t- ",
                      self.battery[cho-1], "mAh\nDisplay \t- ",
                      self.disp[cho-1], "inches")
        elif(ch == 2):
            pass
        else:
            print("\nInvalid Input")


# iadmin is a child class which checks for admin privilages
class iadmin(Mobileinfo):
    def admincheck(self, datab):
        # uname is the username & upass is the password to be entered by admin
        uname = input("User Name : ")
        upass = input("Password  : ")
        if(uname == "akshaysai" and upass == "akshay"):
            print('''Welcome Admin''')
            print('''Admin Privilages are yet to be added''')
        else:
            print("\t\tInvalid Login Credentials")

    # add1mobile is a method using which users can request to add a mobile
    def add1mobile(self):
        mobilenam = input("Enter the name of the mobile you want to request: ")
        self.mobilename.append(mobilenam)
        print("\nThanks for requesting this Mobile. Please give us some time",
              "to add it.\n\n")


# This is the main method where the execution of program starts
def main():
    # Creating objects
    mp = Mobileinfo()
    mp1 = iadmin()
    datab = []
    # This while loop is used to keep on looping until user opts to exit
    while 1:
        print("""
              ======Mobile Phone Guide by Akshay Sai Reddy G=======""")
        print("1. Admin\n2. Customer\n0. Exit")
        privilage = int(input("Enter here : "))
        if(privilage == 1):
            mp1.admincheck(datab)
        elif(privilage == 2):
            while 1:
                print("""
                      1. Display all mobiles list
                      2. Request Admin to add a Mobile's Specification
                      3. View Patter Matching(using Regular Expression)
                      0. Back""")
                choice = int(input("Enter Choice number:"))
                if choice == 1:
                    # Calling method which can print all mobile details
                    mp.displayAvailablemobiles()
                elif choice == 2:
                    # Calling method to let user request to add a mobile
                    mp1.add1mobile()
                elif choice == 3:
                    ''' Example of Pattern matching an email id using
                    Regular Expression'''
                    print("\nPattern Matching for \'akshaysai@gmail.com' is:")
                    print(re.match("[a-z]+@[a-z]+.[a-z]+",
                                   "akshaysai@gmail.com"))
                elif choice == 0:
                    # This break is used to come out of the Customer Privilage
                    break
                else:
                    print("Invalid Input. Please select from below options.")
        elif privilage == 0:
            # This break is used to exit out of program
            break
        else:
            print("Invalid Input. Please select from below options.")

main()
