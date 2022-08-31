# Logical Operators--and,or,not
"""x=100
print(x>50 and x<200)
print(x>500 and x<200)
x=100
print(x>50 or x<20)
print(x>500 or x<50)

x=100
print(not(x>50 and x<200))#true
print(not(x>500 or x<50))#false"""

# Comparison(Relational)->  ==.!=,>,>=,<,<=
import lib2to3.pgen2.token
import re

"""x,y,z=20,30,20
print(x==y)
print(x==z)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)"""

# Compound Assignment(+=,-=,*=,/=,%=)
"""s=100
s+=2 #s=s+2
print(s)"""

# data types
# d=10
# print(type(d))
# a="hai"
# print(type(a))
# x=2.1
# print(type(x))
# c=10j
# print(type(c))
# t=False
# print(type(t))
# l=[1,2,3,4,5]
# print(type(l))
# sl=["hai",'hello',"how are you"]
# print(type(sl))
# tu=('python','java','c')
# print(type(tu))
# dt={1:'anu',2:'ann',3:'anna'}
# print(type(dt))


# formaters in python

# print('a:{a1},b:{b2},c:{c3},d:{d4}'.format(a1=1,b2=3,c3=4,d4="okay"))
#
# print('a:{0},b:{1},c:{2}'.format(1,'three',4))
#
# print('1:{1},2:{0},3:{2}'.format("two",'one',"three"))
# print('{2},{0},{1}'.format(25,15,1))
#
# name="ABHI"
# print("Hellooo, %s !!" %name)


"""name="Aami"
age=20
print("%s is %d years old...." %(name,age))
print('{0} is {1} years old '.format(name,age))"""  # '{0} is {1} years old' is called template
# .format is called format function
# (name,age) is called positional arguments

# Interpolation or string binding
"""print(f'{name} is {age} years old')
mylist=[1,2,3]
print("A list:%s" %mylist)"""

"""x="Red"
print("%s and %s are Colors"%('Green',x))

x=25
str="Variable as Integer=%d \nVariable as Float=%f" %(x,x)
print(str)

y=4+2j
print('real={0} and imaginary={1}'.format(y.real,y.imag))"""

"""n=456
print('Number is {0:f}'.format(n))"""

"""a=567.740
print('Number is {0:.2f}'.format(a))
print('Number is {0:.1f}'.format(a))"""

# Type Casting
"""int()
j=int(12)
a=int(15.76)
h=int('25')
print('{},{},{}'.format(j,a,h))"""

# float()
"""# r=float(15)
# a=float(25.02)
# i=float('2020')
# h=float('25.150')
# print('{},{},{},{}'.format(r,a,i,h))"""

# str
"""r=str('haiii')
e=str(4)
t=str(7.8)
print('{},{},{}'.format(r,e,t))"""

# if....else
"""x=int(input("Enter 1st no:"))
y=int(input("Enter 2nd no:"))
if x==y:
    print("EQUAL")
else:
    print("NOT EQUAL")"""

# Largest of 2 numbers
"""x=int(input("Enter 1st no:"))
y=int(input("Enter 2nd no:"))
if x>y:
    print(x,"is the largest no")
else:
    print(y,"is the largest number")"""

# Even or Odd
"""n=int(input("Enter a number:"))
if n%2==0:
    print(n,'is even number')
else:
    print(n,'is odd number')"""

# Positive,Negative or Zero
"""n=int(input("Enter A Number:"))
if n>0:
    print(n,'is Positive')
elif n<0:
    print(n,'is Negative')
else:
    print('Number is Equal to Zero')"""

# Implement a Calculator
"""a,b=int(input("Enter the 1st number:")),int(input("Enter the 2nd number:"))
opr=input("Enter an Opertor:")
if opr=='+':
    print("Sum is:",a+b)
elif opr=='-':
    print("Differnece is",a-b)
elif opr == '-':
    print("Product is", a*b)
elif opr == '/':
    print("Quotient is", a/b)
elif opr == '%':
    print("Reminder is", a%b)
else:
    print("Invalid Opertor")"""

# Largest of 3 numbers
"""x,y,z=int(input("Enter 1st no:")) , int(input("Enter 2nd no:")) , int(input("Enter 3rd no:"))
if (x>y):
    if(x>z):
        print("Largest no is",x)
    else:
        print("Largest no is",z)
elif y>z:
    print("Largest no is",y)
else:
    print("Largest no is",z)"""

# While Loop
'''print("Natural Numbers")
i=1
while i<=10:
    print(i)
    i=i+1'''

# Odd Numbers upto a limit using while
"""n=int(input("enter a limit:"))
print("odd numbers are:")
i=1
while i<=n:
    if i%2==1:
        print(i)
    i=i+1"""

# Reverse of a number
"""n=int(input("Enter the number:"))
rev=0
while n>0:
    rm=n%10
    rev=rev*10+rm
    n=n//10 #floor division
print("Reverse is",rev)"""

# Pallindrom number
'''n=int(input("Enter a Number:"))
rvs=0
m=n
while n>0:
    r=n%10
    rvs=rvs*10+r
    n=n//10
if m==rvs:
    print("Pallindrom")
else:
    print("Not Pallindrom")'''

# String Reverse
"""str=input("Enter a string:")
r=""
count=len(str)
while count>0:
    r=r+str[count-1]
    count=count-1
print(r)"""

# String Pallindrom
# a=input("Enter a String:")
# rs=""
# b=a
#
# count=len(a)
# while count>0:
#     rs=rs+a[count-1]
#     count=count-1
# if b==rs:
#     print("String is pallindrom")
# else:
#     print("Strings is not pallindrom")


# Products of digits of a number
"""a=int(input("Enter a number:"))
res=1
while a>0:
    b=a%10
    res=res*b
    a=a//10
print("Product is",res)"""

# Armstrong Number
"""a=int(input("Enter a number:"))
res=0
b=a
while a>0:
    c=a%10
    res=res+c*c*c
    a=a//10

if b==res:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")"""

# break statement

# n=1
# while n < 10:
#     n = n + 1
#     if n == 5:
#         break
#     print(n)

# continue statement
"""n=1
while n<10:
    n=n+1
    if n==5:
        continue
    print(n)"""

# pass - it is a null statement
# while 2==3:
#     pass

# for loop
"""a=["Abhirami",25,2,2001]
for i in a:
    print(i)
colors=['Red','Blue','Green']
for item in colors:
    print(item)
for x in 'welcome':
    print(x)"""

# sum of numbers in a list
"""no=[10,20,30]
sum=0
for n in no:
    sum=sum+n
print("Sum is ",sum)"""

# range()
"""for i in range(10):#0,1,2,.....9
    print(i)
for a in range(2,10,3):#2,5,8
    print(a)
for b in range(2,10):#2,3,4,.....9
    print(b)
for c in range(10):#0,1,2,.....9
    print("Hellooo")"""

# list=[2,44,20,49,66,100,29,33,80]
# for i in list:
#     print(i)
#     if i==100:
#         break

# Odd Numbers
"""i=int(input("Enter the limit:"))
print("Odd numbers are:")
for n in range(i+1):
    if n%2==1:
        print(n)"""

# Factorial of a number
"""i=int(input("Enter a number:"))
prd=1
for n in range(1,i+1):
    prd=prd*n
print("Factorial is ",prd)"""

# Fibanocci Series
'''limit=int(input("enter a limit:"))
a,b=0,1
print("Fibanocci Series")
print(a)
print(b)
for n in range(3,limit+1):
    c=a+b
    print(c)
    a,b=b,c'''

# Multiplication table of 5
'''n=int(input("Enter a no:"))
for i in range(1,11):
    print(i,"*",n,"=",i*n)'''

# for loop with else
'''l=[1,2,3,4]
for a in l:
    print(a)
else:
    print("No items left...")'''

# Prime number
'''a=int(input("Enter a number:"))
f=0
for i in range(1,a+1):
    if a%i==0:
        f=f+1
if f==2:
    print("prime")
else:
    print("Not prime")'''

# Nested for
'''a=["Abhi","Arya","Anu"]
b=[100,200,300]
for i in a:
    for j in b:
        print(i,j)'''


# Prime numbers upto a limit
'''a = int(input("Enter a limit:"))
print("Prime numbers are....")
for i in range(2, a + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)'''


#Even numbers upto 15 in reverse order
# for i in range(14,0,-2):
#         print(i)


"""n=int(input("Enter the no of rows:"))           
for i in range(1,n+1):                           
    for j in range(1,i+1):
        print("*",end=' ')
    print()"""

"""
*
* *
* * *
* * * * 
* * * * *
"""


'''a=int(input("Enter a Number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''


'''n=int(input("Enter a Number:"))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=' ')
        k=k+2
    print()'''



'''n=int(input("Enter the number of rows:"))
k=int(input("Enter the ASCII number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end=' ')
    print()'''


'''n=int(input("Enter the no of rows:"))
k=65
for i in range(n):
    for j in range(0,i+1):
        print(chr(k+j),end=' ')
    print()'''


# n=int(input("Enter the no of rows:"))
# k=65
# for i in range(n):
#     for j in range(n):
#         print(chr(k+j),end=' ')
#     print()


'''n=int(input("Enter the no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()'''



"""n=int(input("Enter the no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""



"""n=int(input("Enter the no f rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
for k in range(n-1,0,-1):
    for l in range(1,k+1):
        print(l,end='')
    print()"""



"""n=int(input("Enter the no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*i,end=' ')
    print()"""


# n=int(input("Enter the no of rows:"))
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print()


#String slicing
"""str="Good Night"
s=slice(8)
print(str[s])

t=slice(1,9,2)#1,3,5,7
print(str[t])

r=slice(-1,-7,-2)#-1,-3,-3
print(str[r])"""


#Extending Indexing
"""str='helloooo'
print(str[:5])
print(str[4:])
print(str[1:8:2])
print(str[-6:-3])
print(str[-10:-1:3])
print(str[-1:-7:-2])
print(str[:])
print(str[::-1])"""



"""num=int(input("Enter a number:"))
n=num//2
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("* ",end='')
    for j in range(2*(n-i-1)):
        print(" ",end='')
    for j in range(i+1):
        print("* ",end='')
    print()
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end='')
    for j in range(i,0,-1):
        print("* ",end='')
    print()"""

# num=int(input("Enter a number:"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end='')
#     for j in range(i+1):
#         print("* ",end='')
#     for j in range(2*(num-i-1)):
#         print(" ",end='')
#     for j in range(i+1):
#         print("* ",end='')
#     print()
# for i in range(2*num,0,-1):
#     for j in range(2*num-i):
#         print(" ",end='')
#     for j in range(i,0,-1):
#         print("* ",end='')
#     print()



"""for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or (row==0 or row==3) and (col>0 and col<4):
            print("*",end='')
        else:
            print(end=' ')
    print()"""


#Collections(Array)
"""colors=['Red','Blue','Green','Pink','Yellow','Black']
print(colors[2])
print(colors[-1])
print(colors[2:5])
print(colors[-5:-1])
print(colors[4:])
print(colors[:4])
print(colors[-5:-1])
colors[3]='Indigo'
print(colors)

if 'Blue' in colors:
    print("Item found")
else:
    print("Item not found")

print("Length is ",len(colors))"""


#different functions in list
#items add--append(),insert()
"""lst=['red','blue','green']
lst.append('pink')
print(lst)
lst.insert(2,'Yellow')
print(lst)"""

#items delete--remove(),pop()
"""lst=['red','blue','red','green']
lst.remove('green')
print(lst)
lst.remove('red')
print(lst)

lst=['red','blue','green']
lst.pop()
print(lst)
lst.pop(1)
print(lst)"""


"""lst=['red','blue','green']
lst.clear()
print(lst)
del lst[1]
print(lst)"""



'''L1=[1,2,3,4,5]
L2=[6,7,8,9,10]
L1.append(L2)
print(L1)
print(L1[5])
print(L1[5][2])
L1[5].append(11)
print(L1)
L1[5].insert(4,54)
print(L1)
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)'''



"""a=[1,6,43,89,2,5,88]
a.sort()#ascending order
a.sort(reverse=True)#descending order
print(a)


b=['red','green','violet','blue','gray','pink']
b.sort()#Ascending order
b.sort(reverse=True)#Descending order
print(b)"""


'''l1=[1,2,3,4,5]
l2=l1.copy()
print(l2)

l3=[8,9,10]
l3=l1.copy()
print(l3)'''


"""l=[1,2,3,4,5,6]
print(max(l))
print(min(l))
print(sum(l))"""


"""l=['red','black','blue','pink','white','green']
output=[]
for i in l:
    if 'e' in i:
        output.append(i)
print(output)"""


"""l=['red','white','red','blue','blue','black','yellow']
c=l.count('red')
print(c)

j=[4,10,4,2,3,4,5,8,4]
a=j.count(4)
print(a)"""

"""lst=[]
n=int(input("Enter the no of items:"))
for i in range(0,n):
    item=int(input("Enter Item:"))
    lst.append(item)
print(lst)
l=[]
a=int(input("Enter the no of Items:"))
for i in range(0,a):
    col=input("Enter Items")
    l.append(col)
print(l)
"""


#Tuple
'''mark=(10,20,30)
print(mark)
name=('Abhi','Arya','Athira')
print(name)
print(name[1])
print("Length is ",len(mark))'''

#Change tuple values
"""name=('Abhi','Athira','Gopu')
print(name)
lst=list(name)
lst[2]='Mottu'
names=tuple(lst)
print(names)"""

#Set- unordered,unindexed,{}
"""s={3,7,2,9,10,4}
print(s)
b={3,7,8,9}
print(b)"""

#Dictionary--{},unordered,mutable,indexed,key-value pair
"""d={1:'Java',2:'Python',3:'CPP'}
print(d[2])#key

x=d.get(3)#get() is used to get a value
print(x)"""


# a={'Name':'Abhi','Age':21,'Address':'Ernakulam'}
# b=a.get('Name')
# print(b)
# a['Age']=22
# print(a)
# print(a)
# a['Age']=20
# print(a)
#
# for i in a.keys():#keys()--is used to get all keys
#     print(i)
# for i in a.values():#values()--is used to get all keys
#     print(i)
#
# print("Keys and Values")
# for i,j in a.items():
#     print(i,j)


# l=['red','blue','green','black','pink']
# for i in l:
#     print(i)
#
#
# n=int(input("Enter a limit:"))
# lst=[]
# for i in range(1,n+1):
#     i**=2
#     lst.append(i)
# print(lst)


"""l=[1,2,3]
j=[4,5,6]
print(l+j)"""


'''print([1,2,3,4]==[1,2,3,4])#true
print([1,2,3,4]==[1,2,3,4,5])#False
print([1,2,3,4]!=[1,2,3,4])#False

print([1,2,3,4]>[0])#True
print([1,2,3,4]>[10])#False
print([1,2,3,4]==[1,2,[3,4]])

print([1,2,3,4]==[1.0,2.0,3.0,4.0])#True'''



"""l=[1,2,3,4]
max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print(max)"""


'''a=["py","cppfbjecjice",'z','abhi','html']
print(max(a))
print(min(a))'''


"""a=[[1,2],[3,4],[5,6]]
print(a[1][0])
print(a[-1])"""

#function

# def sum():    #1.Function definition
#     x,y=10,20
#     print("Sum is ",x+y)
#sum()    #2.Function calling

#return value
# def sum():
#     x,y=10,20
#     s=x+y
#     return s
# sm=sum()
# print("sum is",sm)


# def sum(x,y,z):
#     s=x+y+z
#     return s
# sm=sum(10,25,15)
# print("sum is",sm)


"""def fullname(n1,n2):
    name=n1+' '+n2
    return name
fname = input("Enter first name:")
lname = input("Enter last name:")
newname=fullname(fname,lname)
print(newname)"""



"""def sum():
    s=n1+n2
    return s
n1=int(input("1st no:"))
n2=int(input("2nd no:"))
n=sum()
print("Sum is ",n)"""



"""def check():
    return True
if check():
    print("Yes True")
else:
    print("No False")


print(check())

x=check()
print(x)"""



"""def factorial(f):
    prd=1
    for i in range(1,f+1):
        prd=prd*i
    return prd
n=int(input("Enter a Number:"))
if n<0:
    print("Factorial does not exist....")
elif n==0:
    print("Factorial of 0 is 1")
else:
    z=factorial(n)
    print("Factorial is ",z)"""




"""def factorial(f):
    if f==1:
        return 1
    else:
        return (f*(factorial(f-1)))
n=int(input("Enter a Number:"))
if n<0:
    print("Factorial does not exist....")
elif n==0:
    print("Factorial of 0 is 1")
else:
    z=factorial(n)
    print("Factorial is ",z)"""



#arbitary arguments
"""def display(*args):
    print('last no is',args[1])
    for i in args:
        print(i)
display(15,25)"""



"""def display(num,*args):
    print('1st no is',num)
    for i in args:
        print(i)
display(15,25,10)"""


#Keyword arguments
"""def display(c1,c2,c3):
    print("Third one is ",c3)

display(c2='Victor',c3='Roshan',c1='Vimal')"""


"""def display(**kwargs):
    for k,v in kwargs.items():
        print('%s==%s'%(k,v))

display(c2='Victor',c3='Roshan',c1='Vimal')"""


"""def display(arg,*args,**kwargs):
    print("Normal Arguments:",arg)
    print("Arbitary Arguments:")
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print('%s==%s'%(k,v))

display("Kiran","Anju","Ammu",c2='Victor',c3='Roshan',c1='Vimal')"""


"""def display(args1,args2,args3):
    print("Args1:",args1)
    print("Args2:", args2)
    print("Args3:", args3)
x=("PYTHON","JAVA","HTML")
display(*x)"""


"""def display(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
y={'arg1':"Red",'arg2':"Green",'arg3':"Blue"}
display(**y)"""


#default argument/parameter
"""def display(language='PYTHON'):
    print("Our Language is :",language)

display(".Net")
display()"""


#list
"""def display(L1):
    for i in L1:
        print(i)
L=["Rose","Lotus","Jasmine"]
display(L)"""

#Global and Local Variables
# x=100  --global variable
# y=300 --global variable
# def check():
#     x=200  --local variable
#     z=500   --local variable
#     print('Inside value of x is ',x)
#     print('Inside value of y is ',y)
#     print('Inside value of z is ',z)
# check()
# print('Outside value of x is ',x)

"""x=100
def check():
    x=200
    global z
    z=500
    print('Inside value of x is ',x)
    print('Inside value of z is ',z)
check()
print('Outside value of x is ',z)
"""

"""l1=[1,2,3,4]
l2=[1,2,7,8]
outputlist=list(zip(l1,l2))
print(outputlist)

outputlist=dict(zip(l1,l2))
print(outputlist)"""



"""l1=['Anu','Kiran']
l2=[22,23]
l3=['Kollam','Ernakulam']
lst=list(zip(l1,l2,l3))
print(lst)

for n,ag,addr in lst:
    print('%s has %d years old and address is %s'%(n,ag,addr))"""



"""l=[]
def create():
    n=int(input("Enter the no of items:"))
    for i in range(n):
        item=int(input("Enter the number:"))
        l.append(item)
    print(l)

def search():
    m=int(input("Enter an item:"))
    if m in l:
        print("Found")
    else:
        print("Not found")

def  remove():
    a=int(input("Enter the item to be removed:"))
    if a in l:
        l.remove(a)
    else:
        print("Not found")
    print(l)
def replace():
    old=int(input("Enter the item to be replaced:"))
    new=int(input("Enter the new item:"))
    for i in range(len(l)):
        if l[i]==old:
            l[i]=new
    print(l)
# create()
# search()
# remove()
# replace()

while True:
    ch=int(input("1.Create \n2.Search \n3.Remove \n4.Replace \nEnter your choice:"))
    if ch==1:
        create()
    elif ch==2:
        search()
    elif ch==3:
        remove()
    elif ch==4:
        replace()
    else:
        break;"""



"""d={}
def create():
    n=int(input("Enter the no of items in the list:"))
    for i in range(n):
        x=int(input("Enter the key:"))
        y=input("Enter the value:")
        d.update({x:y})
    print(d)
def search_key():
    s=int(input("Enter the key to be searched:"))
    if s in d.keys():
        print("find key")
    else:
        print("Not find")

def search_value():
    val=(input("Enter the value to be searched:"))
    if val in d.values():
        print("find value")
    else:
        print("Not find")

def remove():
    re=int(input("Enter the key to be removed:"))
    if re in d:
        del d[re]
    print(d)

def replace():
    key=int(input("Enter the key to be find:"))
    newval=input("Enter yhe value to be replaced:")
    d[key]=newval
    print(d)

create()
search_key()
search_value()
remove()
replace()"""



"""a="Python is easy to learn"
print(a.split())
print(a.split('n'))


txt = "apple#banana#cherry#orange"
print(txt.split('#'))
"""


# print(100==100)
# print(100 is 100)



#lambda functions
"""s=lambda a:a+10
print(s(20))
b=s(50)
print(b)"""


#lambda expression can take more than one arguments
"""x=lambda a,b:a*b
print("Product is ",x(2,4))"""


"""odd=lambda x:(x%2==1)
n=int(input("Enter the number:"))
h=odd(n)
if h:
    print("odd")
else:
    print("even")"""


#filter()
#Program to filter out even numbers from a list
"""l=[1,2,3,4,5,6]
x=list(filter(lambda x:(x%2==0),l))
print(x)"""

#map()
"""l=[10,9,8,7]
x=list(map(lambda x:(x**2),l))
print(x)"""

#reduce()
"""from functools import reduce
l=[1,2,3,4,5]
p=reduce(lambda x,y:x*y,l)
print(p)"""

# l=[2,3,4,5]
# l=[6,4,5]
# l=[24,5]
# 120

# class student:
#     pass

"""class student:
    name="Abhi"
obj=student()
print(obj.name)"""


"""class A:
    def display(self):
        print('simple function')
    def sum(s,a,b):
        print("sum is",a+b)
obj=A()
obj.display()
obj.sum(15,25)"""



"""class B():
    def fact(self,num):
        f=1
        for i in range(1,num+1):
            f=f*i
        print("factorial is",f)
obj=B()
obj.fact(4)"""

"""class A():
    def display():
        print("Without self variable")
    def check(self):
        print("With self variable")
obj1=A
obj1.display()

obj2=A()
obj2.check()"""


#Constructors
#non-parameterized constructor
"""class student:
    def __init__(self):
        print("Non Parameterized Constructor")
ob=student()"""

#parameterized constructor
"""class student:
    def __init__(self,name):
        print("Name is",name)
obj=student("Abhi")"""


"""class student:
    def __init__(self,name,id,place):
        self.n=name
        self.i=id
        self.p=place
        print("Name is",self.n)
        print("ID is",self.i)
    def user(self):
        print('Place is',self.p)
object=student("Mottuzz",345,"vypin")
object.user()"""


"""class student:
    def __init__(self,name):
        self.n=name
object=student("Mottuzz")
print("Name is",object.n)"""



"""class student:
    def __init__(s,name):
        s.n=name

    def user(x):
        print('name is',x.n)
object=student("Mottuzz")
object.user()"""



"""class student:
    def __init__(se,id):
        se.i=id

    def user(self):
        print("ID is", self.i)
object=student(345)
object.user()

object.i=22
print("Changed ID is",object.i)"""


#COUNTING THE NUMBER OF OBJECTS
"""class student:
    count=0
    def __init__(self):
        student.count=student.count+1

obj=student()
obje=student()
print("Count is",student.count)"""

#SUM OF 2 NUMBERS
"""class Sum:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def result(s):
        print("Sum is",s.n1+s.n2)
n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))
obj=Sum(n1,n2)
obj.result()"""


"""class person:
    def __init__(self):
        self.name="Abhi"
    def display(self):
        print("Name is",self.name)
    class dob:
        def __init__(self):
            self.dd=25
            self.mm=2
            self.yy=2001
        def display(self):
            print("DOB is:{}/{}/{}".format(self.dd,self.mm,self.yy)


obj=person()
obj.display()
obj1=obj.dob()
obj1.display()"""





#Destructors
"""class student:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("object deleted")
obj=student()
del obj"""

#Inheritance
#Single Inheritance
"""class A:
    def display1(self):
        print("Base Class")
class B(A):
    def display2(self):
        print("Derived Class")
obj=B()
obj.display1()
obj.display2()"""


"""class A:
    def display(self):
        self.a = int(input("1st no:"))
        self.b = int(input("2nd no:"))
class B(A):
    def displayB(self):
        print("Sum is",self.a+self.b)

obj=B()
obj.display()
obj.displayB()"""

#Mutli-level Inheritance
"""class A:
    def display(self):
        self.a=int(input("1st no:"))
        self.b=int(input("2nd no:"))
class B(A):
    def sum(self):
        self.c=self.a+self.b
        print("Sum is",self.c)
class C(B):
    def avg(self):
        print("Average is",self.c/2)
obj=C()
obj.display()
obj.sum()
obj.avg()"""


"""class A:
    def student(self):
        self.a=input("Enter Name:")
        self.b=int(input("Enter Age:"))
        self.c=int(input("Enter Ph no:"))
class B:
    def details(self):
        self.d=input("Enter Qualification:")
        self.e=input("Enter University:")
        self.f=int(input("Enter Marks:"))
class C(A,B):
    def print(self):
        print("Student Details")
        print("Name:",self.a)
        print("Age:",self.b)
        print("Ph Number:",self.c)
        print("Qualification:",self.d)
        print("University:",self.e)
        print("Marks:",self.f)

obj=C()
obj.student()
obj.details()
obj.print()"""




"""class A:
    def read(self):
        self.a=int(input("Enter 1st no:"))
        self.b=int(input("Enter 2st no:"))
class B(A):
    def sum(self):
        self.c=self.a+self.b
        print("Sum is",self.c)
class C(A):
    def avg(self):
        self.d=(self.a+self.b)/2
        print("Average is",self.d)
class D(A):
    def prd(self):
        self.e=self.a*self.b
        print("Product is",self.e)

obj1,obj2,obj3=B(),C(),D()
obj1.read()
obj1.sum()
obj2.read()
obj2.avg()
obj3.read()
obj3.prd()"""


"""from abc import ABC,abstractmethod
#abstract class
class Polygon(ABC):
    #abstract method
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("Non Abstract Method")

class Triangle(Polygon):
    def sides(self):
        print("Triangel has 3 sides")

t=Triangle()
t.sides()
t.display()"""


#Polymorphism
#Function Overloading
"""class Name:
    def display(self,name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")
obj=Name()
obj.display()
obj.display("Abhi")"""



"""def add(dataype,*args):
    if dataype=='int':
        answer=0
    if dataype=='str':
        answer=''
    for x in args:
        answer=answer+x
    print(answer)

add('int',2,5)
add('str','hiii','hello')"""


#Function Overriding
"""class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def getArea(self):
        print("Area is",self.l*self.b)
class Square:
    def __init__(self,side):
        self.s=side
    def getArea(self):
        print("Area of square is",self.s*self.s)
obj=Square(4)
obj.getArea()"""


# super()
"""class Computer():
    def __init__(self,computer1,ram1,storage1):
        self.computer2=computer1
        self.ram2=ram1
        self.storange2=storage1
class Mobile(Computer):
    def __init__(self,computer,ram,storage,memory1):
        super().__init__(computer,ram,storage)
        self.memory=memory1
Apple=Mobile("Apple",4,512,"Iphone 13")
print("Computer is",Apple.computer2)
print("Ram is",Apple.ram2)
print("Storage is",Apple.storange2)
print("Memory is",Apple.memory)"""



#List Comprehension
#square
"""l=[i*i for i in range(1,5)]
print(l)"""

#Even number
"""l=[i for i in range(1,11) if i%2==0]
print(l)"""


"""a=[x for x in "hai hello how r you" if x in ['a','e','i','o','u']]
print(a)"""


"""l1=[1,2.5,'abhi',3,1.5,25]
l2=[a for a in l1 if type(a)==float]
print(l2)"""

"""l=[1,-2,3,12,-24,-298,35,215]
l2=[x for x in l if x>0]
print(l2)"""


"""str=["Apple","Bat","Cat","Dog"]
l=[len[0] for len in str]
print(l)"""



"""colors=['red','blue','green','pink']
lst=[x for x in colors if 'e' in x]
print(lst)
l=[x for x in colors if x!='blue']
print(l)
l1=[x.upper() for x in colors]
print(l1)
l2=['haii' for x in colors]
print(l2)
l3=[x if x!='green' else 'yellow' for x in colors]
print(l3)"""


"""t=[lambda x=x:x*10 for x in range(1,11)]
for i in t:
    print(i())"""


#Exception Handling
"""try:
    x=int(input("Enter 1st no:"))
    y=int(input("Enter 2nd no:"))
    z=x/y
    print(z)
except ZeroDivisionError as a:
    print(a)
except ValueError as b:
    print(b)

except Exception as e:
    print("Exception",e)"""


#List Comprehension Example
"""matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)"""


"""lis = [num for num in range(100) if num % 5 == 0 if num % 10 == 0]
print(lis)"""



#Regular Expression******************************************************
#findall()--returns a list containing all matches
import re
# txt="red and green and blue"
# x=re.findall('and',txt)
# print(x)

# str='sun mon tue wed thu fri sat'
# x=re.findall(r'[sat]',str)
# print(x)

# st='sat mat pat rat cat'
# l=re.findall(r'[spr]at',st)
# print(l)

# st='sat mat pat rat cat'
# l2=re.findall(r'[^spr]at',st)
# print(l2)

# s='33456896754'
# l=re.findall(r'\d{1,2}',s)
# print(l)

# s='32432 543 324 4577'
# l1=re.findall(r'\b\d{3}',s)
# print(l1)
# l2=re.findall(r'\b\d{3}\b',s)
# print(l2)





# Search--It is used to search the string for a match and returns a match object
"""txt="Haii helloo hw r u 21"
x=re.search('\s',txt)
print(x)
print(x.start())
y=re.search('\d',txt)
print(y.start())
z=re.search('hw',txt)
print(z.start())
a=re.search('hii',txt)
print(a)"""



"""str='What is your name'
f=re.search('^What.*name$',str)
if f:
    print("yes")
else:
    print("no")"""


#Split()
"""str='red and blue are colors'
d=re.split(' ',str)
print(d)
x=re.split('e',str)
print(x)"""

"""str='yellow,green and,red are colors'
y=re.split(',',str)
print(y)"""

"""str='red and blue are colors'
z=re.split('\s',str,3)
print(z)"""


#sub()
"""import re
txt='Red and Blue are colors'
x=re.sub('\s','@',txt)
print(x)

y=re.sub('\s','%',txt,2)
print(y)"""



#Email validation
"""import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

e= input("Enter a email id:")
check(e)"""



#Phone number validation
"""import re
regex='^[6-9]+\w{9}$'
def check(num):
    if (re.search(regex,num)):
        print("Valid")
    else:
        print("Invalid ")

n= input("Enter a Phone number:")
check(n)"""



#Pincode Validation
"""import re
regex='([0-9]{6}|[0-9]{3}\s[0-9]{3})'
def check(pin):
    if (re.search(regex,pin)):
        print("Valid")
    else:
        print("Invalid ")

n= input("Enter a Pin code:")
check(n)"""



#FILE HANDLING******************************************************************************************************************

# f=open('prgmfile.txt','r')
# print(f.read())
# print(f.read(6))
# print(f.readline())
# for i in f:
#     print(i)
# f.close()

# f=open('prgmfile.txt','a')
# f.write('hello...')
# f.close()
#
# f=open('prgmfile.txt','r')
# print(f.read())

# f=open('prgmfile.txt','w')
# f.write("Welcomeeee...")
# f.close()
#
# f=open('prgmfile.txt','r')
# print(f.read())


#seek()****************************************************************************
"""f=open('prgmfile.txt','r')
f.seek(3)
print(f.read())"""


#tell()***************************************************************************
"""f=open('prgmfile.txt','r')
l=f.readline()
position=f.tell()
print('Position is ',position)
f.close()"""


"""def test(fname):
    with open(fname) as f:
        contents=f.readlines()
        print(contents)
test('prgmfile.txt')"""


"""from shutil import copyfile
copyfile('prgmfile.txt','dest.txt')"""



#enumerate()
"""days={'mon','tue','wed'}
print(list(enumerate(days)))
print(list(enumerate(days,4)))"""



"""def file_len(fname):
    with open(fname) as f:
        for i,j in enumerate(f,1):
            pass
        return i
print('length is',file_len('prgmfile.txt'))"""


# class A:
#     def __init__(self,name,age):
#         self.name=name#public
#         self.__age=age#private
#         #self._age=age#protected
#
#     def display(self):
#         print(self.name)
#         print(self.__age)
# obj=A("Abhi",21)
# obj.display()
# print(obj.name)
# print(obj._A__age)#name mangling
# # print(obj.__age) #error



# import pymysql
# dbCon=pymysql.connect(host='localhost',user='root',password='Abhirami@2001',database='python')
# cobj=dbCon.cursor()
#
# id=int(input("Enter Id:"))
# name=input("Enter Address:")
# sal=input("Enter salary:")
#
# sql="insert into emp values(%s,%s,%s)"
# val=(id,name,sal)
#
# cobj.execute(sql,val)
# dbCon.commit()
# print("Inserted")


# lst= ["A", "B", "C"]
# str= "java"
#
# print(list(enumerate(lst)))
# print(list(enumerate(str)))


# l=[1,2]
# if len(l)==0:
#     print("No items")
# else:
#     print("Items present")



# def print_sum_even_nums(even_nums):
#     total = 0
#
#     for x in even_nums:
#         if x % 2 != 0:
#             break
#
#         total += x
#     else:
#         print("For loop executed normally")
#         print(f'Sum of numbers {total}')
#
#
# # this will print the sum
# print_sum_even_nums([2, 4, 6, 8])
#
# # this won't print the sum because of an odd number in the sequence
# # print_sum_even_nums([2, 4, 5, 8])


# import math
# print(math.floor(23.2))
























