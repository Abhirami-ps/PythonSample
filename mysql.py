import pymysql
dbCon=pymysql.connect(host='localhost',user='root',password='Abhirami@2001',database='python')
cobj=dbCon.cursor()

##############################.......INSERT.......##############################
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


##############################.......UPDATE.......##############################


# name=input("Enter name:")
# id=int(input("Enter Id:"))
#
# sql="update emp set Empname='%s' where Id=%d"%(name,id)
# cobj.execute(sql)
# dbCon.commit()


##############################.......SELECT.......##############################

# id=int(input("Enter Id:"))
# sql="select * from emp where Id=%d"%id
# cobj.execute(sql)
# i=cobj.fetchone()#Fetch only one row
# print("Id=",i[0])
# print("Empname=",i[1])
# print("Salary=",i[2])



# sql="select * from emp"
# cobj.execute(sql)
# alldata=cobj.fetchall()
# for i in alldata:
#     print("Id=",i[0])
#     print("Empname=",i[1])
#     print("Salary=",i[2])


##############################.......DELETE.......##############################

# id=int(input("Enter Id:"))
# sql="delete from emp where Id=%d"%id
# cobj.execute(sql)
# dbCon.commit()

"""for i in range(-10,0,1):
    print(i)




numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)"""



"""num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)




n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()"""



# l=[10,20,30]
# l.sort(reverse=True)
# for i in l:
#     print(i)



"""start =int(input("Enter start"))
end = int(input("Enter End"))
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)"""




"""my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i)"""

# n=int(input("Enter a range"))
# m=int(input("Enter a range"))
# for i in range(n,m+1):
#     print("Cube is",i*i*i)


# a=[10,20,30]
# b=[25,15,10]
# if a[0]==b[-1]:
#     print("True")
# else:
#     print("False")



#
# list1 = ["M", "na", "i", "Abh"]
# list2 = ["y", "me", "s", "i"]
# list3 = [i + j for i, j in zip(list1, list2)]
# for i in list3:
#     print(i,end=' ')


"""list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)"""





"""list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)"""



# a=[10,20,20,26,30,30,20]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)



try:
    a = int(input("Enter a no:"))
    b = int(input("Enter a no:"))
    c = a / b
    print(c)

except Exception as e:
    print("Exception",e)




















