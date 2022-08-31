"""print("HAI...")
a=10
print(a)
a = 'red'
print(a)
b = "blue"
print(b)"""


# s = "Abhirami"
# r = "P S"
# print("Full Name:"+s+" "+r)


"""n1=10
n2=20
print("Sum is",n1+n2)
x,y,z=10,20,30
print(x,y,z)"""


# a = b = c = 100
# print(a, b, c)


# x=input("enter your name:")
# print(x)
# y=input("Enter a number:")
# print(y)
# z1=int(input("Enter 1st Number:"))
# z2=float(input("Enter 2nd Number:"))
# print(z1+z2)


"""s=int(input("1st no:"))
t=int(input("2nd no:"))
print("sum is",s+t)
print("Difference is",s-t)
print("Multiplication-",s*t)
print("division-",s/t)
print("modulus-",s%t)
print("exponent is",s**t)
print("floor division",s//t)"""


# x,y=int(input("Enter a number:")),int(input("Enter a number:"))
# temp=x
# x=y
# y=temp
# x,y=y,x#multiple values to multiple variables
# print("X=",x,",","Y=",y)
# print("{} {},{} {}".format("value of x is:",x,"value of y is:",y))



# a=int(input("Enter a no:"))
# f=0
# for i in range(1,a+1):
#     if a%i==0:
#         f=f+1
# if f==2:
#     print("Prime")
# else:
#     print("Not")



"""my_stack = []
# append() function to push
# element in the my_stack
my_stack.append('x')
my_stack.append('y')
my_stack.append('z')
print(my_stack)

# pop() function to pop
# element from my_stack in
# LIFO order
print('\nElements poped from my_stack:')
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

print('\nmy_stack after elements are poped:')
print(my_stack)"""











"""queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)"""

# ****************************************************************************
"""even or odd
def even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
n1=int(input("Enter no:"))
even(n1)
"""


"""def reverse(n):
    rev=0
    while n>0:
        rs=n%10
        rev=rev*10+rs
        n=n//10
    print("Reverse is",rev)
num=int(input("Enetr no:"))
reverse(num)"""


"""def prime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    if f==2:
        print("Prime")
    else:
        print("Not")
num=int(input("Enter a no:"))
prime(num)
"""

# **********************************************************************************

#Threading

"""from time import sleep
from threading import Thread
def task():
    print("Wait for a moment")
    sleep(3)#milliseconds
    print("This is from another thread")

# task()
th=Thread(target=task())
th.start()
"""


#passing arguments
"""from time import sleep
from threading import Thread
def task(sleep_time,msg):
    print("Wait for a moment")
    sleep(sleep_time)
    print(msg)

th=Thread(target=task,args=(3,"Haiii...Helloo..."))
th.start()"""


#multi-threading
"""import time
import threading

def calc_squ(num):
    print("Calculate the square root of a given number")
    for n in num:
        time.sleep(0.3)
        print("Square is",n*n)

def calc_cube(num):
    print("Calculate the cube of a given number")
    for n in num:
        time.sleep(0.3)
        print("Cube is",n*n*n)

arr=[2,3,4]
t=time.time()
# calc_squ(arr) #call calc_squ() function
# calc_cube(arr) #call calc_cube() function
th1=threading.Thread(target=calc_squ,args=(arr, ))
th2=threading.Thread(target=calc_cube,args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()

print("Total time taken by threads is",time.time()-t)"""

"""class A:
    def factorial(self,num):
        prd=1
        for i in range(1,num+1):
        
        
            prd=prd*i
        print("Factorial is",prd)

ob=A()
ob.factorial(4)
"""




