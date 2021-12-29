             # introduction to function.

# fxn to add two nummber.
def add_two(num1,num2):     # to define fxn use def keyword & here num1 and num2 are called parameter.
    return num1+num2

num1=int(input("enter first integer number: "))
num2=int(input("enter second integer number: "))
print(add_two(num1,num2))   # fxn calling & here num1 and num2 are called arguments.
          
# OR

print("\n")

a=20
b=5
c=sum((a,b)) # by using sum (built-in function) function.
print(c)          


# function to return last char. of string.
def last_char(name):
    return name[-1] # [index ie. here last index.]

print(last_char("Govind Gupta"))


# function to print odd or even.
def odd_even(num):
    if num%2==0:
        return "number is even."
    else:
        return "number is odd."

# eshme (else:) ko hta de aur return waley line ko ek tab space back krr de tb bhi same output aayega.    

i=float(input("enter any number to check even or odd: "))
print(odd_even(i))


# above same function in pythonic way..
def is_even(num):
    return num%2 == 0 # here return in boolean form ie. True or False.

i=int(input("enter any number: "))
print(is_even(i))


# Use of function and Docstring..
def function1(a,b):
    print("Hii, you are in function 1.",a+b)

def function2(a,b):
    """This is function which will calculate average of two numbers.""" # this is called doc string.
    average =(a+b)/2
    print(average)
    return average

v=function2(5,9)
print(v)

# to print docstring use this syntax...
print(function2.__doc__)


# fxn to check greatest.
def greatest_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return (f" {num1} is greatest among all.")
    elif num2>num1 and num2>num3:
        return (f"{num2} is greatest among all.")
    else:
        return (f"{num3} is greatest among all.")

number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
number3=int(input("enter third number: "))
print(greatest_num(number1,number2,number3))      


# fxn to print fibonacci series.
def fibonacci_series(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end = " ")

user_input=int(input("enter the number to where find fibonacci series: "))
print(fibonacci_series(user_input))            

# Program to print Palindrome..
# Palindrome - words that reads same backwords as forwards ie. example - madam, naman.
def is_pelindrome(word):
    reversed_word = word[::-1] # yha se reversed_word ko bhi hta satey hain dono jagah se,
    if word == reversed_word:  # aur wha if word == word[::-1]: likh saktey h..jaise niche comment are liha hoo..
#   if word == word[::-1]:   
        return True
    return False # else: hta saktey h..

i=input("Enter the string: ")
print(is_pelindrome(i))


# Default parameter...
# jis variable me default value dal denge ushe right k sbhi variable me default value hona chahiye.
def user_info(first_name,last_name = 'unknown',age=25): # here last_name, age is default value. 

    print(f"Your first name is: {first_name}")
    print(f"Your last name is: {last_name}")
    print(f"Your age is: {age}")

user_info("Govind","Gupta") # here if you give age as 18 then print your is 18(see below).
#user_info("Govind","Gupta","18")


# Scope of variables in function and outside of function..
x=5            # Global variable.
def func():
    global x   # use of global value to change its value ie.x=5 to x=7 but normally not do this..
    x=7        # local variable.
    return x

print(x)
print(func())
print(x)





