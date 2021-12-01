# Make flexible functions by using - *args ,**kwargs ,lambda ,Enumerate(), 
#map(), filter(), iterables & iterator, zip(), any(), all()....


# function with all parameters..
# use parameters in given below order...PADK..ie.
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


#  use of * (star) operator ie. *args means ,,, use of touple data type.
def all_total(*args): # function declaration using * operator..
    total = 0
    for num in args:
        total +=num
    print(type(args)) # args has scope inside loops..
    return total    
    
print(type(all_total))
print("Sum of total is: ",all_total(1,2,3,4,5,6,10,56,55))        


#  *args with normal parameter...
# args takes argument as touple.

def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print("Multiply of given numbers are: ", multiply_nums(2,2,3))
l1=(2,4,3)
print("Multiply of list-1 is: ",multiply_nums(*l1))



# kwargs (keyword argument)
# **kwargs (double star operator)
# kwargs take argument as a dictionary.

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(first_name ='Govind', last_name = 'Gupta')



            # lambda expressions (anonymous function)

add2 = lambda a,b : a+b
print(add2(3,7))

x= lambda a,b : a*b
print(x(4,5))


# uses of lambda w.r.t. other function..

def is_even(a):
    if a%2==0:
        return(True)
    else:              # else ko remove bhi krr satey hain..
        return False

print(is_even(5))

# OR same above program is:

def is_even1(b):
    return b%2==0 # this return True or False..

print(is_even1(10))

# OR above same program using lambda..

is_even2 = lambda c : c%2==0
print(is_even2(5)) 


# use of if- else with lambda expression..

def func(s):
    if len(s)>5:
        return True
    return False

print(func("Govind"))

# OR

def func(s):
    return len(s)>5

print(func('abc'))

# OR above program using lambda..

func1 = lambda s : True if len(s)>5 else False
print(func1("Gupta"))

# OR  above same program without if-else..

func2 = lambda s: len(s) >5
print(func2('abcdefg'))


        # Uses of enumerate() function..
# We use enumerate() function with for loop to trac position of our item in iterable ..  

names=["govind", "gupta", "good"]
for position, name in enumerate(names):
    print(f"{position}-------> {name}")

# Without using enumerate function..
print("\n")

names = ['Govind', "Gupta", "Pravin", "good", "holiday","Gandhiji" ]
position = 0
for name in names:
    print(f"{position} ----> {name} ")
    position +=1


# uses of map() function...

numbers = [1,2,3,4]

def square(a):
    return a**2

print(square(2))
squares =list(map(square,numbers))
print(squares)

# OR 
print("\n")

numbers = [1,2,3,4]
squares = list(map(lambda a:a**2,numbers))
print(squares)

# OR above program using list comprehension..

squares_new = [i**2 for i in numbers] # yha numbers wala value ko square krr rha h..
print(squares_new)

x = [i**2 for i in squares] # yha squares wala value ko square krr rha h..
print(x)


print("\n")
# using map function find the length of string..

names =["Govind", "Gupta", 'abc', 'abcd', 'abcde']
length = list(map(len,names))

print(length)



# uses of filter function..
def is_even(a):
    return a%2==0

numbers=[3,4,5,2,6,8,7,1,9]
evens = tuple(filter(is_even,numbers))
print("Even numbers of your list is: ",evens)
  # OR Nichey waley me function definition a use nhi hain..
x= tuple(filter(lambda b:b%2 != 0,numbers))
print("Odd numbers of your list is: ",x)
y=tuple(filter(lambda a:a%2==0,numbers))
print("Even number of your list is: ",y)


# Concepts of iterator vs iterables..
num=[1,2,3,4,5,6] # list, tuples, string --> iterables
squares=map(lambda a:a**2,num) # iterator

#for j in num:
 #   print(j)

# How iterables works..
number_iter=iter(num)
print(next(number_iter))
print(next(number_iter))  # these lines from 190 to 196
print(next(number_iter))  # is same as upper for loop..
print(next(number_iter))  # these lines show how for loops works..
print(next(number_iter))
print(next(number_iter))
print(num)

#for i in squares:
 #   print(i)

# How iterator works...    
print(squares)
print(next(squares))
print(next(squares))  # these lines from 203 to 209
print(next(squares))  # is same as upper for loop..
print(next(squares))  # these lines show how for loops works..
print(next(squares))
print(next(squares))


# uses of zip function..
# zip()--> used to combine the lists(many list) or dictionary(only two list see line 220) and form tuple..

user_id =['user1','user2','user3'] # ydi ek user_id remove krr de to kya print hoga try it..
names=['Govind','Arvind','Pravin']
last_names = ["Gupta", 'gupta','yadav']

print(list(zip(user_id,names,last_names))) # converted to list using "list" keyword...
print(dict(zip(user_id,names))) # converted to dictionary using "dict" keyword..


# uses of reverse zip function(of just above program)...
l = [(1,0),(2,9),(3,8),(4,7),(5,6)]
print(list(zip(*l)))
l1,l2=(list(zip(*l)))
print(list(l1))
print(list(l2))


# uses of any() & all() function..
nums = [2,4,6,8,0]
even =[]
for num in nums:
    even.append(num%2==0)

print(even)
print(all([True, True, True, True, True]))
print(any([False,False,False,False,False]))
print(any([False,True,False,False,False]))
print(all([False,True, True, True, True]))

