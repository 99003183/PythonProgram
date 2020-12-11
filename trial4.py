import sys
class Mobiephone:
    def __init__(self):
        self.mobilenames=["1. Samsung S20FE","2. Samsung M51","3. Samsung A51"]
        self.RAM=["8","6/8","4/6/8"]
        self.ROM=["128","128","64/128"]
        self.proce=["Exy990","Sd730G","Exy9611"]
        self.battery=[4500,7000,4000]
        self.disp=[6.4,6.7,6.5]

    def displayAvailablemobiles(self):
        print("")
        print("The mobiles we have in our library are as follows:")
        for mobile in self.mobilenames:
            print(mobile)
        print("")
        print("""Want to view specifications of a mobile?
        1. Yes
        2. No""")
        ch=int(input("Enter Choice: "))
        if(ch==1):
            cho=int(input("Select the Mobile from list above: "))
            print("")
            print(self.mobilenames[cho-1],"\nRAM - ",self.RAM[cho-1],
                  "GB\nROM - ",self.ROM[cho-1],"GB\nProcessor - ",
                  self.proce[cho-1],"\nBattery - ",self.battery[cho-1],
                  "mAh\nDisplay - ",self.disp[cho-1],"inches")
            
    def add1mobile(self):
        mobilename=input("Enter the name of the mobile you'd like to add: ")
        self.mobilenames.append(mobilename)
        print("Thanks for adding mobile name")
    
def main():            
      mp=Mobiephone()
      done=False
      while done==False:
            print(""" 
                      ======Mobile Phone Guide by Akshay Sai Reddy G=======
                  1. Display all mobiles list
                  2. Add Mobile
                  0. Exit""")
            choice=int(input("Enter Choice:"))
            if choice==1:
                mp.displayAvailablemobiles()
            elif choice==2:
                mp.add1mobile()
            elif choice==0:
                sys.exit()
            else:
                print("Invalid Input. Please select from below options.")
                  
main()