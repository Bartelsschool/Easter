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
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 

def again():
   return "Y" or "N"



print("What's your operation?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#operation based on user choice
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
#relief valve
else:
   print("Invalid input. Do you want to try again?")

def choice():
    input("Enter choice(1/2/3/4):")
again = input("Do you want to calculate again? Please type Y for YES or N for NO")
if again.upper() =='Y': 
   choice()
elif again.upper() =='N': 
   print("Thanks for trying")


