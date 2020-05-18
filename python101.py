#print(3+3)
#print(100*2+6)
#print(100*2+6/3.5%4)
#y = x/7
#print(y)
#z = y*2
#f = y/2
#print(f)
#print('calculating the number of pay periods')
#print('in a year')
#print('Answer is 26')
#input
#age = int(input("How old are you?"))
#print('Your age is', age)
#print('You have', 65 - age, 'years until retirement')
#print("Welcome to May")
#month_number = int(input("How many months have have gone by so far? "))
#print(12 - month_number, "more months to end 2020")
#basic loops"
#for a in range (2,4):
 #   print(a, "cubed is", a*a*a)
 #end
#for b in range (1,10):
 #   print (b, "the even numbers under 20 are", b*2)
 #end
 #  adding for loop with else to a range(start,stop,step_size)
#for x in range (1,10):
#   print(x, "the odd numbers are",(x*2)-1)
#end


#building a calculator application with for loops


#defining 
#def is function
#decimals are floats whole numbers are integers. commas mean space
#def add(x, y):
  #  return x + y

#def subtract(x, y):
  #  return x - y

#def multiply(x, y):
  #  return x * y

#def divide(x, y):
 #   return x / y 

#def again():
  # return "Y" or "N"



#print("What's your operation?")
#print("1.Add")
#print("2.Subtract")
#print("3.Multiply")
#print("4.Divide")
#choice = input("Enter choice(1/2/3/4):")


#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#operation based on user choice
#if choice == '1':
 #  print(num1,"+",num2,"=", add(num1,num2))

#elif choice == '2':
  # print(num1,"-",num2,"=", subtract(num1,num2))

#elif choice == '4':
 #  print(num1,"/",num2,"=", divide(num1,num2))

#elif choice == '3':
  # print(num1,"*",num2,"=", multiply(num1,num2))
#relief valve
#else:
  # print("Invalid input. Do you want to try again?")

#def choice():
 #   input("Enter choice(1/2/3/4):")
#again = input("Do you want to calculate again? Please type Y for YES or N for NO")
#if again.upper() =='Y': 
  # choice()
#elif again.upper() =='N': 
 #  print("Thanks for trying")








#code to see how many Nintendo Wiis a user can purchase. 

#price of a Nintendo Wii is 80 dollars

#def ans1():
   #return "Y" or "N"
#print("Hi there! Do you want to know how many Nintendo Wiis can you purchase?")
#print("type Y for yes or N for No")
#if ans1 =='Y':


'''
print("Hi there! Do you want to know how many Nintendo Wiis can you purchase?")

choice = input("Enter choice(Y/N):")
#operation based on user choice
if choice == 'Y':
   print("How much money do you have in your savings account?")
elif choice =='N':
   print("have a good day then")

#defining variables
cost_of_a_nintendo_wii_in_us_dollars = 80
nintendo_wii_budget = int(input("in US Dollars: "))
purchaseable_number = int(nintendo_wii_budget/cost_of_a_nintendo_wii_in_us_dollars)
cost_of_a_nintendo_wii_in_us_dollars = 80
remaining_budget = cost_of_a_nintendo_wii_in_us_dollars-nintendo_wii_budget
#num5 = purchaseable_number

if cost_of_a_nintendo_wii_in_us_dollars == nintendo_wii_budget:
   print("My friend, you can buy only one Nintendo Wii.")
if cost_of_a_nintendo_wii_in_us_dollars<nintendo_wii_budget:
   print("You can buy",purchaseable_number,"Nintendo Wiis")
if cost_of_a_nintendo_wii_in_us_dollars>nintendo_wii_budget:
   print("you need",remaining_budget,"US Dollars more to afford one.")
'''



#lesson 4 
#for_loops

for x in range(1,10):
  print(x,"multiples of 2 are", 2 * x)
  print(x,"multiples of 3 are", 3 * x)
  print(x,"multiples of 4 are", 4 * x)
 