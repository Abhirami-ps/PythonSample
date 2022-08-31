#Renaming the module
"""import exampleModule as exmod
exmod.display()
exmod.sum()"""



"""import exampleModule
exampleModule.display()
exampleModule.sum()

na=exampleModule.student['Name']
ag=exampleModule.student['Age']
mk=exampleModule.student['Mark']
print(na)
print(ag)
print(mk)"""



#Built-in modules (eg-platform,math,etc..)
"""import platform
print(platform.system())

import math
print(math.sqrt(64))"""



"""from exampleModule import student
print("Name is ",student['Name'])

from exampleModule import sum
sum()

from exampleModule import *
display()
sum()
print("Age is ",student['Age'])"""




"""import listModule
while True:
    ch=int(input("1.Create \n2.Search \n3.Remove \n4.Replace \nEnter your choice:"))
    if ch==1:
        listModule.create()
    elif ch==2:
        listModule.search()
    elif ch==3:
        listModule.remove()
    elif ch==4:
        listModule.replace()
    else:
        break;"""



from listModule import *
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
        break;
