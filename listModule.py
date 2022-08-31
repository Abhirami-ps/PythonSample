l=[]
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