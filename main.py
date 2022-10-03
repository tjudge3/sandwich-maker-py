#2022-02-24
from datetime import datetime
import calendar
today = datetime.today() 
#The imports aren't actually utilized in the user part of the program itself, however they were the easiest way to show an example to the user. I wasn't sure if using calender.month_name with the user input would have satisfied the requirements of the assignment. 
monthNum=0
def monthName(monthNum): #here we create our function, a list of month names that correspond to a number
    if(monthNum == 1): return "January"
    if(monthNum == 2): return "February"
    if(monthNum == 3): return "March"
    if(monthNum == 4): return "April"
    if(monthNum == 5): return "May"
    if(monthNum == 6): return "June"
    if(monthNum == 7): return "July"
    if(monthNum == 8): return "August"
    if(monthNum == 9): return "September"
    if(monthNum == 10): return "October"
    if(monthNum == 11): return "November"
    if(monthNum == 12): return "December"
def main():
  print("Welcome the the Months of the Year Program\n")
  print("In this program you will enter a number between 1 and 12 and get the corresponding month name\n")
  print("For example, the current month number we are in is", today.month, "and the current month name is:", calendar.month_name[today.month])
#The three prints above is all intro information explaining how the program works
  if __name__ == "__main__": #since we're working with some libraries we're using this to make sure the code is being run here and not imported
    while(True): #Here we have our loop, while the condition is true.
        print("Please enter a number between 1 and 12: ""\n\r")
        monthNum = int(input())#Here we are asking the user to input a number between 1 and 12
        if(monthNum < 1 or monthNum > 12): #if the number is not between one and twelve we inform the user that there is a problem and loop back asking them to input a number again 
            print("\n\r""Sorry, but the number must be between 1 and 12. Let's try that again!""\n\r")
        else:
            break #if the number is in our range we break out of the loop and pass along the user input.
    print("\n\r""The month name is " + (str)(monthName(monthNum))) #Here we print the month name (monthName) that coresponds to our user inputted month number (monthNum)
  restart = input("Would you like to do that again? (Press Y to restart) ")
  if restart.upper() == "Y": #loop back to the start
    main()
  print("Goodbye")
  exit() #exit the program
main()
#
#If the month name function wasn't needed (which I think it was for the assignment - 2 functions), I would have justed not had that list at all and made line 33 the following: 
#print("\n\r""The month name is " + (str)(calendar.month_name[(monthNum)]))