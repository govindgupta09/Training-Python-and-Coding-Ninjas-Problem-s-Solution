                # Basics of python...!! and Operators..


print("Hello World..!!")
print("Govind Gupta")
print("hello world!",end=" , ") #  end(newline character merge next line.) comma at end and prints next line on same line.
print("Hii Govind..!! \' How are you.") # see the uses of escape sequence.
print('Twinkle,twinkle,little star,\n How I wonder what you are!\t \"Up above the world so high, \\ Like a diamond in the sky.')


print("this is single \\ back slash.")
print("this is double \\\ back slash.")
print(r"this is double \\ back slash.") # by putting r in starting escape sequence removed.

print("/\\/\\/\\/\\ this is mountain.")
print("he is \t awesome.")  # use of back slash tab.
print("\\\" \\n \\t \\\' \n This is the result of above line program.")      # \\ = \ and \' = (').


# code to print emoji in python from 01 to 999.
print("\U0001F601") 
print("\U0001F602")
print("\U0001F603")
print("\U0001F604")
print("\U0001F620")
print("\U0001F644")
print("\U0001F999")



var1="hello "
var2,var3,var4,var5=34,20.5,"55","11"  # variables declared in single line.
print(type(var1))
print(type(var2))   # to know the type of variable ie Datatypes.
print(type(var3))
print(type(var4))
print(var2+var3)    # plus(+) sign between two """string""" used for concatenation.
print(var1+var4)
# print(var3+var4)  # it is an error bcoz string add with only string.
print(int(var4)+int(var5))  # typecast the var4 from string to integer type ,also string() and float() used for typecasting..
print(10*"Govind Gupta\n")    # 10 times my name is printed.
print(10 * str(int(var4) + int(var5)))



# below are the three different way of printing the same line.
name,age = "Govind Gupta", "18"  # declaration of multiple variable in single line.
print("Hii " + name + " your age is  "+ age) # string add with string only.
print("Hello {} your age is {}".format(name,age)) # string formetting & arithmetic calcultion also used.
print(f"hello {name} your age is {age}") # string formeting & arithmetic calculation also used.


print("enter your number:")
inpnum=input() # by default inpnum me string value store hogi.
print("you enter the number:",inpnum)
#print("you enterd :",inpnum+10) # wrong bcoz inpnum is string & 10 is integer so add not takes place.
print("your enterd value + 10 is:",int(inpnum)+10)



# simple program to add two numbers..
num1=input("enter first number for addition:")
num2=input("enter second number to add:")
print(num1 + num2) # concatanation takes place.
print(float(num1)+float(num2))

# OR above program in this way..

print("enter first number:")
num1=input()
print("enter second number:")
num2=input()
print("Sum of first & second number is:", int(num1)+int(num2))


# string concatanation.
first_name = "Govind"
last_name = "Gupta"
full_name = first_name + " " + last_name
print(full_name)
print(full_name + " is " +str(19)+ " years old.")   # or write "18"



# some standard fxn in python & uses of string , string is collection characters..
mystr ="my name is Govind Gupta." # Space also included.
print("Length of your string is:",len(mystr))
print("String from 0 to 23 is:",mystr[0:23])  # string slicing--> syntex-[start:stop-1]
print("String after skip one to one character:",mystr[0:24:2])# advanced string slicing.
print("Reverse of your string govind Gupta is:",mystr[::-1])# syntex-[start:stop-1:step] , kuchh nhi likhne pr start me 
 # by default 0 value & stop me length of string le lega & step me by default 1 le lega kyuni by dafault one hi hota h.
print("Reverse of your string govind Gupta by skip one to one character is:",mystr[::-2])
print("Is your string end with a. :",mystr.endswith("a."))
print("Is your string ends with Gupta :",mystr.endswith("Gupta")) # False bcoz full stop not used.
print("Number of G in your string is: ",mystr.count("G"))
print("Capitalise the first word of your string.",mystr.capitalize())
print("By replacing is by are in my string:",mystr.replace("is","are"))
print("Position of the n in your string is:",mystr.find("n"))
print("My string in upper case is:",mystr.upper())
print("My string in lower case is:",mystr.lower())
print("Is your string is all numeric :",mystr.isalnum()) 
print("Is your string is alphanumeric :",mystr.isalpha()) # spaces in string ,so this is not alpha.



# program to swap two numbers..

a=5
b=3
print("Number before swaping:",a,b)
a,b=b,a
print("Number after swaping:", a,b)



# uses of List (ordered & mutable) and their methods...

numbers=[2,3,7,4,5,15,20] # square bracket for List.. 
print("Number List is :",numbers)
numbers.append(8)
print("Number 8 add at the end of list by using append function:")
print(numbers)
print("Numbers after slicing:",numbers[1:5:])
numbers.insert(2,17)
print("Insert number 17 at index 2:",numbers)
numbers.pop(2)
print("After deleting number at index 2:",numbers)
numbers.remove(3)
print("After removing 3 from the numbers list:",numbers)
numbers.sort()
print("Numbers after sorting (increasing order):",numbers)
numbers.reverse()
print("Numbers after reverse:",numbers)
print(numbers)



# uses of Touple (ordrerd & immutable) and their methods..
# a1=()   :--> empty touple.
# a2=(3,)   :-->touple with only one element need a comma.
tpl =(1,2,5,3,4,7,3,8,10,15,3,20,3,17,11) # paranthesis for Touple.
print(tpl)
print("Index number of element 7 is:",tpl.index(7))
print("Total number of 3 is:",tpl.count(3)) 
print("Index number of 3 (first) is:",tpl.index(3)) 
print("lenth of touple is:",len(tpl))
print("Max. of touple is:" ,max(tpl))
print("Minimum of touple element is:",min(tpl))
print("Sum of touple element is:",sum(tpl))
print("Sorting (increasing order) of touple element is:" ,sorted(tpl))



# Uses of Dictionary (unordered & mutable), Dictionary is nothing but a key value pairs.
d1= {}
print(type(d1))
print(d1.keys())
print("\n")

d2={"Govind":"Burger",
"Krishna":"Roti",
"Pravin":"Maggie","Mritunjay":"Biryani","Shivanand":"Fish & Chawal"}
print(d2.keys())
print(d2.items())
print("\n")

d2.update({"Shubham":"Toffee"})
print(d2.keys())
print(d2.items())
print("\n")

print("Key value of item Govind is:",d2.get("Govind"))



# uses of set (unordered & mutable) and their methods..

s=set()
print("Type of s is:",type(s))
s_from_list=set({1,2,3,4,5,5})
print(s_from_list)
print("Type of s_from_list is:",type(s_from_list))


# Simple introduction program..
print("enter your name:")
name=input()
print("you enter your name is",name)
name=input("what is your name:") # input fxn takes always and only string value.
print("my name is " + name)
age=input("what is your age:")
print("You typed your age is: "+age)
print("\n")



# program to find perimeter of triangle..
var1,var2=8,5
perimeter=2*(var1+var2)
print("perimeter of given rectanle is: {}".format(perimeter))


# program to count occurance of given character..
string = "Govind Gupta"
print(string.count("G"))


# Program is to add two number. 
n1=input("enter the first number to add  ")
n2=input("enter the second number to add  ")
print("sum of these two numbers is",int(n1)+int(n2))


                # Operators...

# Arithmetic Operators (+, -, *, /, //, **)
# Assignment Operators (=, +=, /=, *=)
# Comprison Operators  (==,!= , > ,< ,<= ,>=)
# Logical Operators    (True , False ,NOT, AND , OR ,)
# Identity Operators   (is , is not)
# Bitwise Operators    (Bitwise NOT , AND , OR , XOR ,XNOR)
# Membership Operators  (in , not in)

# uses of and & or operator.
name,age=input("enter your name and age:  ").split() 
print(f"your name is {name} and age is {age} ") 
if age>="18" and (name[0]=="G" or name[0]=="g"):
    print("you can watch this movie.")
else:
    print("sorry! you can't watch this movie.") 



a=10
b=66
print(a+b)
print(a/b)
print(a//b)
print(b/a)
print(b%a)

print(2+3)
print(2-3)
print(2*3)
print(3/2)     # float division.
print(3//2)    # integer division.
print(2**3)    # double multiply symbol used as exponent. 
print(5%2)     # remainder after division.
x=y=z=1        # x=1,y=1,z=1 in this line.
print("sum of x,y and z is:" + str(x+y+z))





