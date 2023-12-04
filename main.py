#Working with Arrays
import pyinputplus, calendar, re
from datetime import date
curr_date = date.today() #imports above to help make the magic happen
sandw_foods = [{'White': '$1.75', 'Wheat': '$1.11', 'Whole Wheat': '$1.15', 'Multigrain': '$1.15', 'Whole Grain': '$1.75', 'Sprouted Grain': '$1.11', 'Sourdough': '$1.55', 'Rye': '$1.55', 'Pumpernickel': '$1.31', 'Brioche': '$2.11', 'Challah': '$2.25', 'Flatbread': '$1.51'},
 {'Smoked Turkey': '$.75', 'Honey Roasted Turkey': '$1.11', 'Chicken': '$1.15', 'Smoked Ham': '$1.15', 'Honey Baked Ham': '$1.75', 'Roast Beef': '$1.11', 'Corned Beef': '$1.55', 'Bologna': '$2.51', 'Salami': '$1.31', 'Pastrami': '$2.11', 'Liverwurst': '$2.25', 'Vegan Beef': '$1.51'},
 {'American': '$2.75', 'Swiss': '$1.11', 'Cheddar': '$1.15', 'Blue Cheese': '$1.15', 'Manchego': '$1.75', 'Gruyere': '$1.11', 'Brie': '$1.55', 'Mozzarella': '$3.51'},
 {'Bacon': '$1.51','Lettuce': '$1.65','Tomato': '$1.79','Eggs': '$1.98','Onions': '$1.31','Bell Peppers': '$1.15','Olives': '$1.53','Cuucumbers': '$1.25'},
 {'Mustard': '$1.51','Mayo': '$1.65','Ketchup': '$1.79','Tartar Sauce': '$1.98','Wasabi': '$1.31','Olive Oil': '$1.15','Soy Sauce': '$1.53','Relish': '$1.25'}]
#Here we have our lists of the various food options that are presented to the customer and done in conjunction with the food prompts below. If this program was going to production, I'd probably tell people that they can simply edit the options above based on what they want to add or remove
sandw_foods_prompts = ['What type of roll would you like?:','What type of meat would you like?:','Do you want cheese?(yes/no)','Do you want filling?(yes/no)','Do you want condiments?(yes/no)','How many sandwiches do you want?:']
#Here we have a list of our sandwich prompts that go through in order          
order = [] #we define order
total_cost = 0 #We set the total cost to zero
print("Welcome to Milliways, better known as The Restaurant at the End of the Universe. We hope you're having a wonderful " +calendar.day_name[curr_date.weekday()]+"\n\r") #we print a welcome message and reference hitchhikers guide to the galaxy. We add the day of the week it creates a feeling of comfort
order_email = pyinputplus.inputEmail(prompt=' Please Enter Your Email Address: ')
#Here we ask for their email and validate that it is an email. It's outside the order form so we get their email anyway. Like a real business.
san_order = pyinputplus.inputYesNo(prompt='Would you like a sandwich? ')#we ask if they like to order a sandwich - if they say yes, we begin the program, if not we send it to the bottom, thank them and quit
if san_order  == 'yes': #they have said yes, so now we begin
  def millways_sandw(fprompt, choice, yn): #we create our millways sandwich function 
    if fprompt: #the fprompt is the sandw_foods_prompts, it pulls them in and display the list of questions before the various options
        print(fprompt)
    if yn == True: #if they choose yes as an option (true) then return or go to the yes/no prompt
        return pyinputplus.inputYesNo(prompt='') #here we validate the yes/no
    elif yn == False: # if they choose no as an option (false) then we run on to the next which is the inputmenu of the various food choice items from the list above
        return pyinputplus.inputMenu(
            [k + ' ' + v for k, v in sandw_foods[choice].items()], 
            numbered=True, prompt='') #here we are presenting the various food options based on the specific food item from above
    elif yn == 'end': #here if chosen not to get more we end our menu and begin the calculations
     #below we use range len to create our list of items so they can be numbered correctly and then if a number is outside the list we tell them that it's not a valid choice
        return pyinputplus.inputInt(min=1, prompt='')    
  for i in range(len(sandw_foods_prompts)): 
    if i <= 1:
        order.append(millways_sandw(sandw_foods_prompts[i], i, False))
    elif i in range(2,5): #here and the next two (non comment) lines we have our yes/no prompts that ask for cheese, filling and condiments
        if millways_sandw(sandw_foods_prompts[i], i, True) == 'yes':
            order.append(millways_sandw('', i, False))
    elif i == 5:  #here and the next 3 (non comment) lines we get the total cost of the sandwich and multiply it by the total number of sandwiches chosen. We use the float to full conform with the rubic
        total_sandwiches = millways_sandw(sandw_foods_prompts[i], i, 'end')
  for i in [re.sub(r'[^0-9.]', '', i) for i in order]:#this could be done without regular expressions but since it was being used in the final it made sense to try to incorporate it into the program, much the same was the calendar/datetime was utilized here
     total_cost += float(i) * total_sandwiches #we use total cost rather than just "cost" since it would be a variable we'd use if we were adding additional items like soup or drinks or whatnot.   
  print(f'Thank you '+(order_email)+' your order is confirmed')#here we print their email address as their "name" that we got above
  print(f'Total price: $ {round(total_cost, 2)}') #here we print the total price of all the options together and number of sandwhiches
elif san_order  == 'no':#if they said above that they don't want to order a sandwich, we come down here, thank them for stopping by, tell them they should come again and quit the program
  print('No problem. Thanks for stopping by. Please come again.\n')
  quit()#we quit the program and kill the repl process
