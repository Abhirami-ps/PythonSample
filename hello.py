"""
a = input("enter 2 no:")
b = input()
print("hellooooo"+a + "second value" + b)
sum=(int(a)+int(b))
print("result is"+str(sum))"""



# no1=int(input("enter 1st no:"))
# no2=int(input("enter 2st no:"))
# no3=int(input("enter 3st no:"))
# average=(no1+no2+no3)/3
# print("averahe is",str(average))


#swapping
# a=input("enter a value")
# b=20
# print(type(a))
# print(type(b))
# t=a
# a=b
# b=t
# print(a)
# print(b)


# a=int(input("enter a no"))
# b=int(input("enter a no"))
# print("sum is",a+b)


# a="hai,how are you"
# print(a[-8:-1])



# name="abhirami"
#
# names=["abhi","arya","sini","sunil"]
# names[0]="abhirami"
#
# # print(names[2:])
# names=names+["abhirami"]
# names.append('hai')
# names.append(input("enter a value"))
# print(names)


# logical operator
# x=100
# print(x>150 and x<200)
# # comparison
# x,y=100,200
# print(x!=y)
# # compound assignment
# a=10
# a+=2
# print(a)
# # data types
# b=(10,29,25)
# print(type(b))
# # formaters
# p="abhi"
# q="arya"
# print("{} {}".format(p,q))
# print()
# print(f"name is {p} {q}")
# print("%s and %s are names"%(p,q))
# print('{1} and {0}'.format(p,q))
# print('a:{0},b:{1}'.format('Abhi','Arya'))
# intrepolation

# largest of 2 numbers
# x,y=int(input("Enter 1st no:")),int(input("Enter 2nd no:"))
# if x>y:
#     print(x)
# else:
#     print(y)
# even or odd
# x=int(input("Enter a no:"))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")

# +ve,-ve or 0
# x=int(input("Enter a no:"))
# if x>0:
#     print("Positive")
# elif x<0:
#     print("Negative")
# else:
#     print("Zero")
# simple calculator
# x,y=int(input("Enter 1st no:")),int(input("Enter 2nd no:"))
# opr=input("Enter Operator:")
# if opr=='+':
#     print(x+y)
# elif opr=='-':
#     print(x-y)
# elif opr=='*':
#     print(x*y)
# elif opr=='/':
#     print(x/y)
# else:
#     print("Invalid")
# largest of 3 no
# x,y,z=int(input("Enter 1st no:")),int(input("Enter 2nd no:")),int(input("Enter 3rd no:"))
# if x>y:
#     if x>z:
#         print(x)
#     else:
#         print(y)
# elif y>z:
#     print(y)
# else:
#     print(z)
# 1st 10 natural numbers
# print("Natural Numbers.....")
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# odd numbers upto numbers
# n=int(input("Enter the limit:"))
# print("Odd numbers are....")
# i=1
# while i<n:
#     if i%2==1:
#         print(i)
#     i=i+1
# reverse a no
# n=int(input("Enter a no:"))
# rev=1
# while n>0:
#     rm=n%10
#     rev=rev*rm
#     n=n//10
# print(rev)
# pallindrome
# n=int(input("Enter a no:"))
# rev=0
# m=n
# while n>0:
#     rm=n%10
#     rev=rev+rm*rm*rm
#     n=n//10
# if m==rev:
#     print('Armstrong')
# else:
#     print('Not')
# string reversal
# a=input("Enter a String:")
# r=""
# b=a
# count=len(a)
# while count>0:
#     r=r+a[count-1]
#     count=count-1
# if r==b:
#  print(r,"is Pallindrome")
# else:
#     print("Not")
# string pallindrome
# product of digits of numbers
# armstrong
# break,continue,pass
# i=0
# while i<10:
#     i=i+1
#     if i==5:
#         continue
#     print(i)
# for loop
# a=['abhi','arya']
# for i in a:
#     print(i)
# range
# for i in range(1,11):
#     print(i)

# for loop with break
# z=[1,2,3,4,12,45,67]
# for i in z:
#     print(i)
#     if i==3:
#         break
# odd numbers
# n=int(input("Enter the limit:"))
# for i in range(1,n+1):
#     if i%2==1:
#         print(i)
# factorial
# n=int(input("enter a no:"))
# prd=1
# for i in range(1,n+1):
#     prd=prd*i
# print(prd)
# fibanocci
# n=int(input("Enter a limit:"))
# a,b=0,1
# c=0
# print(a)
# print(b)
# for i in range(3,n+1):
#     c=a+b
#     print(c)
#     a,b=b,c


# multiplication table
# for with else
# prime or not
# nested for
# prime numbers upto a limit
# n=int(input("Enter no of rows:"))
# k=65
# for i in range(n):
#     for j in range(n):
#         print(chr(k+j),end=' ')
#     print()


# for i in 'hai':
#     print(i)
# b=[12,34,45]
# for j in b:
#     print(j)
# a=[1,2,3]
# sum=1
# for i in a:
#     sum=sum*i
# print(sum)
# n=int(input("Enter a limit:"))
# print("Even numbers are....")
# for i in range(2,n+1,2):
#     print(i)
# a=[10,2,2,3,3,4,4,6,7,3,5]
# for i in a:
#     if i==4:
#         break
#     print(i)
# n=int(input("Enter a No:"))
# p=1
# for i in range(1,n+1):
#     p=p*i
# print(p)
# n=int(input("Enter a no:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
# n=int(input("Enter a number:"))
# prd=1
# for i in range(1,n+1):
#     prd=prd*i
# print(prd)
# n=int(input("Enter a limit:"))
# a,b=0,1
# print("Fibanocci Series....")
# print(a)
# print(b)
# for i in range(3,n+1):
#     i=a+b
#     print(i)
#     a,b=b,i
# a=[10,20,30]
# for i in a:
#     print(i)
# else:
#     print("No items left...")
# x=int(input("Enter a Number:"))
# flag=0
# for i in range(1,x+1):
#     if x%i==0:
#         flag=flag+1
# if flag==2:
#     print("prime")
# else:
#     print("Not prime")
# n=int(input("Enter a limit:"))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
# n=int(input("enter no of rows:"))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print()
# a="GOOD EVENING"
# s=slice(-1,-7,-1)
# print(a[s])
# print(a[-7:-2])
# i=['red','blue','green','orange','yellow','pink','black']
# del i[5]
# print(i)
# i.remove('blue')
# print(i)
# i.clear()
# print(i)
# print(len(i))
# if 'green' in i:
#     print("Yes")
# else:
#     print("no")
# i.sort()
# for j in i:
#     print(j)
# a=['red','blue','green','yallow']
# c=[]
# for i in a:
#     if 'e' in i:
#         c.append(i)
#         c.sort()
# print(c)
# l=[]
# a=int(input("Enter no of items:"))
# for i in range(0,a):
#     b=input("Item:")
#     l.append(b)
#     l.sort()
# print(l)
# n=int(input("Enter no of items:"))
# l=[]
# for i in range(1,n+1):
#     i=i*i
#     l.append(i)
# print(max(l))
# print(l)
# n=int(input("Enter no of items:"))
# l=[]
# for i in range(0,n):
#     c=input("Enter Item:")
#     l.append(c)
# print(l)

# colors=["Red","Blue","Green"]
# colors.sort()
# print(colors)

# a = (15,2,25,9,21,20)
# x = sorted(a)
# print(x)

# fruits = ["Mango","Apple","Orange"]
# fruits.reverse()
# print(fruits)
#
# a=[1,2,3,3,2,5,7,3]
# a.reverse()
# print(a)

# a = ["Kochi", "Banglore", "Chennai", "Mumbai"]
# b= reversed(a)
# for x in b:
#   print(x)

# fruits = ["Mango","Apple","Orange"]
# x=fruits.index("Apple")
# print(x)

# x = bool(0)
# print(x)

# x = list(("Red","Blue","Green"))
# print(x)



# class A:
#     def read(self,a,b):
#         self.a=a
#         self.b=b
# class B(A):
#     def sum(self):
#         self.c=self.a+self.b
#         print("Sum is",self.c)
# class C(A):
#     def avg(self):
#         self.d=(self.a+self.b)/2
#         print("Average is",self.d)
# class D(A):
#     def prd(self):
#         self.e=self.a*self.b
#         print("Product is",self.e)
# a=int(input("Enter 1st no:"))
# b=int(input("Enter 2nd no:"))
# obj1,obj2,obj3=B(),C(),D()
# obj1.read(a,b)
# obj1.sum()
# obj2.read(a,b)
# obj2.avg()
# obj3.read(a,b)
# obj3.prd()


# x = dict(one = "ONE", two = "TWO", three = "THREE")
# print(x)

# x = pow(4,5)
# print(x)

# x = bin(15)
# print(x)

# x = round(4.244235,2)
# print(x)

# x = abs(-9.25)
# print(x)

# mylist = [False, True, False]
# x = any(mylist)
# print(x)

# x = isinstance(4.5,float)
# print(x)

# x = ascii("I am from Americå")
# print(x)



#PRODUCT OF 2 NUMBERS
"""class product:
    def __init__(self,n1,n2):
        self.a=n1
        self.b=n2
    def display(s):
        print("Product is",s.a*s.b)
n1=int(input("1st no:"))
n2=int(input("2nd no:"))
obj=product(n1,n2)
obj.display()"""

#EVEN OR ODD
"""class no:
    def __init__(self,n):
        self.num=n
    def number(s):
        if s.num%2==0:
            print("Even")
        else:
            print("Odd")
n=int(input("Enter a no:"))
object=no(n)
object.number()"""


#Simple calculator
"""class cal:
    def __init__(self,a,b,op):
        self.n1=a
        self.n2=b
        self.opr=op
    def calc(s):
        if s.opr=='+':
            print("Sum is",a+b)
        elif s.opr=='-':
            print("Difference is",a-b)
        elif s.opr=='*':
            print("Product is",a*b)
        elif s.opr=='/':
            print("Quotient is",a/b)
        else:
            print("Invalid")
a=int(input("1st no:"))
b=int(input("2nd no:"))
op=input("Enter operator:")
obj=cal(a,b,op)
obj.calc()"""

#First 10 natural numbers
"""class num:
    def __init__(self):
        i = 1
        print("natural numbers")
        while i<=10:
            print(i)
            i=i+1
object=num()"""

#swapping two 1st and last element in a list
"""l=[1,2,3,4,5,6]
l[0],l[-1]=l[-1],l[0]
print(l)"""


#Spiderman
"""from turtle import *

speed(13) # Painting speed control
bgcolor("#990000")
pensize(10)
penup()
goto(0,50)
pendown()
circle(-120)
penup()
circle(-120,-60)
pendown()
pensize(5)
right(50)
circle(70,55)
right(85)
circle(75,58)
right(90)
circle(70,55)
right(90)
circle(70,58)

# body
penup()
pensize(10)
goto(80,15)
pendown()
seth(92)
fd(135)
seth(125)
circle(30,135)
seth(190)
fd(50)
seth(125)
circle(30,135)
seth(275)
fd(90)

# Arm 1
penup()
pensize(10)
goto(92,-150)
seth(240)
pendown()
fd(80)
left(10)
circle(-28,185)

# Arm 2
penup()
goto(0,50)
seth(0)
pensize(10)
circle(-120,-60)
seth(200)
pendown()
fd(72)
left(20)
circle(30,150)
left(20)
fd(20)
right(15)
fd(10)
pensize(5)
fillcolor("#3366cc")
begin_fill()
seth(92)
circle(-120,31)
seth(200)
fd(45)
left(90)
fd(52)
end_fill()
fd(-12)
right(90)
fd(40)
penup()
right(90)
fd(18)
pendown()
right(86)
fd(40)
penup()
goto(-152,-86)
pendown()
left(40)
circle(35,90)
# Body coloring
penup()
goto(-80,116)
seth(10)
pensize(5)
pendown()
begin_fill()
fillcolor("#3366cc")
fd(155)
seth(-88)
fd(37)
seth(195)
fd(156)
end_fill()
penup()
goto(-75,38)
seth(15)
pendown()
begin_fill()
fd(158)
seth(-88)
fd(55)
seth(140)
circle(120,78)
end_fill()
# Arm 1 To color
penup()
fillcolor("#3366cc")
pensize(5)
goto(75,-170)
pendown()
begin_fill()
seth(240)
fd(30)
right(90)
fd(17)
end_fill()
fd(10)
left(80)
fd(55)
penup()
left(90)
fd(15)
pendown()
left(85)
fd(55)
penup()
goto(43,-225)
left(84)
pendown()
circle(60,51)
speed(0)

# Body vertical lines
for i in range(3):
  penup()
  goto(-70+i*15,135)
  seth(-90)
  pendown()
  pensize(5)
  fd(15-2*i)

for i in range(3):
  penup()
  goto(36 + i * 15, 156)
  seth(-90)
  pendown()
  pensize(5)
  fd(15 - 2 * i)
  a = -60
  b = 70

for i in range(4):
  penup()
  goto(a,b)
  a=a+40
  b=b+10
  seth(-90)
  pendown()
  pensize(5)
  fd(26)

def oo (li,jing):
  penup()
  goto(0,50)
  seth(0)
  circle(-120, li)
  pendown()
  right(jing)
  pensize(5)
  oo(-60,110)
  fd(130)
  oo(-28,96)
  fd(140)
  oo(9,89)
  fd(144)
  oo(42,70)
  fd(160)
  oo(80,60)
  fd(130)
  penup()
  goto(-80,-40)
  right(160)
  pendown()
  right(50)
  circle(70,45)
  right(75)
  circle(70,38)
  right(50)
  circle(70,45)
  right(90)
  circle(70,48)
  penup()
  goto(-53,-70)
  pendown()
  left(40)
  circle(70,30)
  right(50)
  circle(70,20)
  right(50)
  circle(70,38)
  right(70)
  circle(70,24)
  penup()
  goto(-19,-105)
  left(72)
  pendown()
  fd(22)
  right(60)
  fd(22)
  oo(-140,80)
  circle(-90,120)
  penup()
  oo(140,100)
  circle(90,13)
  pendown()


right(-50)
circle(70,45)
right(75)
circle(70,38)
right(50)
circle(70,36)
penup()
goto(22,-185)
right(70)
pendown()
fd(72)
penup()
goto(-40,-182)
right(38)
pendown()
fd(70)
speed(10)
# The left eye
penup()
pensize(7)
goto(-15,-110)
seth(0)
pendown()
pensize(10)
begin_fill()
left(130)
fd(110)
right(250)
circle(90,60)
circle(40,120)
fillcolor("#F5FFFA")
end_fill()

# Right eye
penup()
goto(5,-110)
pendown()
begin_fill()
right(30)
fd(110)
right(-250)
circle(-90,60)
circle(-40,120)
end_fill()
done()"""



