            #  Conditional statements in Python..

# uses of if-else statement.
age=int(input("enter your age:"))
if age>=18: # may be use parenthesis --> (age>=18):
    print("you can vote..!!") # Tab space in starting is called "indentation"..
else:
    print("sorry..!! you are underage..!!,")
    print("you can't vote..!!")


# Short-hand of if-else..
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b: print(f"{a} is greater then {b}.") # short form of if statement..
else: print(f"{a} is smaller then {b}")  # short form of else statement..
print(F"{b} is greater then {a}.") if a<b else print(f"{a} is greater then {b}.") # short-hand of if-else.


# Program to check which number is greater among four..
num1=input("enter first number: a = ")
num1=int(num1)
num2=int(input("enter second number: b = "))
num3=input("enter third number: c = ")
num4=input("enter forth number: d = ")
num3=int(num3)
num4=int(num4)
if num1>num2 and num1>num3 and num1>num4:
    print("a = {} is greater to all.".format(num1))
elif num1<num2 and num2>num3 and num3>num4:
    print("b = {} is greater to all.".format(num2))
elif num1<num3 and num2<num3 and num3>num4:
    print("c = {} is grater to all.".format(num3))
else:
    print("d = {} is greatest number.".format(num4))


# uses of if-elif-else statement..
age=input("please, enter your age..! ")
age=int(age)
if age==0 or age<0:
    print("sorry! you can't watch mov ie.")
elif 10<=age<20:
    print("your movie ticket charge is Rs.100 ")
elif 20<=age<50:
    print("your movie ticket charge is Rs.250 ")
elif 50<=age<=70:
    print("your movie ticket charge is Rs.500 ")
else:
    print("you have no charge.")                


# use of "in" and "not in".
user_input=input("enter any word:   ")
alphabet= input("enter an alphabet you want to check that is present in word or not. ")
if alphabet in user_input:
    print(f"{alphabet} is present in {user_input}. ")
else:
    print(f"sorry! {alphabet} is not present in {user_input}. ")    


list=[2,5,7,5,3,8,6,9,0]
print(15 in list) # false..
print(15 not in list) # True..
print("No, its not in the list.")
print(6 in list)  # true..
if 5 in list:
    print("Yes..! its in the list.")

