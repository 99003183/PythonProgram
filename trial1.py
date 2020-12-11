import sys
class Library:
      def __init__(self,listofmobiles):
            self.availablemobiles=listofmobiles

      def displayAvailablemobiles(self):
                   print("The mobiles we have in our library are as follows:")
                   print("================================")
                   for mobile in self.availablemobiles:
                         print(mobile)
     # def lendmobile(self,requestedBook):
      #      if requestedBook in self.availablebooks:
       #           print("The mobile you requested has now been borrowed")
       #           self.availablebooks.remove(requestedBook)
        #    else:
        #          print("Sorry the mobile you have requested is currently not in the library")
                  
      def add1mobile(self,returnedBook):
          self.availablemobiles.append(returnedBook)
          print("Thanks for adding mobile")
            

class Student:
      def requestmobile(self):
            print("Enter the name of the mobile you'd like to borrow>>")
            self.mobile=input()
            return self.mobile

      def addmobile(self):
            print("Enter the name of the mobile you'd like to add: ")
            self.mobile=input()
            return self.mobile

def main():            
      library=Library(["Samsung S20FE","Samsung M51","Samsung A51"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all mobiles list
                  2. Add Mobile
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablemobiles()
            elif choice==2:
                        library.add1mobile(student.addmobile())

            elif choice==4:
                  sys.exit()
                  
main()