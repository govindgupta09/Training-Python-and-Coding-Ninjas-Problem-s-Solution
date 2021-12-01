                 # uses of loops..

# Simple python program by for loop.
'''
for i in range(11):          
    print("Govind Gupta", i)   # Tab space is necessary. 

print("\n")

for i in range(10):
    print(f"Govind Gupta : {i} ")    

print("\n")

for i in range(16):
    if i==11:
        continue
    print("number is: ",i)


# Uses of for loop..
list1=[1,4,5,8,9,6,2,10,15,12,"Govind","Gupta"]
for item in list1:
    if str(item).isnumeric() and item >=5:
        print(item)


# use of while..
i=0
while i<=20:
    print("Govind Gupta..!!",i)
    if i==15:
        break
    i=i+1

a=int(input("enter the number less then 100 :"))
while True:  # while 1: bhi likh satey hain..
    if a<=100:
        print(f"Your entered number is :",a)
        a+=1    
'''

while True:
    inp=int(input("Enter a number:\n"))
    if inp>=100:
        print("Congrats you have entered a number greater then or equal to 100.")
        break
    else:
        print("Try again:\n")
        continue

# Program to add integer numbers up to n.
n=input("Enter the integer to where you want sum: ")
n=int(n)
i=0
total=0
while i<=n:
    total=total+i     # total += i
    i += 1            # i = i+1
print(total) 

# above same program by using for loop.
n=input("enter the integer to where you want sum: ")
n=int(n)
total=0
i=0
for i in range(1,n+1):  
    total += i    
print(total)


# programm to add the digit place of number.
num=input("enter any number: ")
total=0
i=0
while i<=len(num)-1:
    total+= int(num[i])
    i=i+1
print(total)  

#above same program by using for loop.
num=input("enter the number:")
total=0
for i in range(0,len(num)):
    total += int(num[i])
print(total)    





