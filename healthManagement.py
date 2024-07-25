#health management system
print("Welcome to our health management system!")

def getdate():
    import datetime
    return datetime.datetime.now()

x=int(input("Press 1 to log in the entry and 2 to retrieve about the client's data:"))
n1=int(input("Press 1 for exercise data and 2 for food nutritions:"))
print("1. Harry")
print("2. Rohan")
print("3. Hammad")
n2=int(input("please enter the number as per the client's name:"))

if x==1:
    if n1==1 and n2==1:
        f=open("harryEx.txt","a")
        h=input("please enter the exercises you want to add for harry:\n")
        time=str(getdate())
        f.write(f"({h}+[+{time}+]+\n")
        f.close()
    elif n1==1 and n2==2:
        f2=open("rohanEx.txt","a")
        r=input("please enter the exercises performed by rohan:")
        time=str(getdate())
        f2.write(f"({r}+[+{time}+]+\n")
        f2.close()
    elif n1==1 and n2==3:
        f3=open("hammadEx.txt","a")
        hd=input("please enter the exercises performed by hammad:")
        time=str(getdate())
        f3.write(f"({hd}+[+{time}+]+\n")
        f3.close()

    elif n1==2 and n2==1:
        ff=open("harryDiet.txt","a")
        d1=input("please enter the additional diet for harry:\n")
        time=str(getdate())
        ff.write(f"({d1}+[+{time}+]+\n")
        ff.close()
    elif n1==2 and n2==2:
        ff1 = open("rohanDiet.txt", "a")
        d2 = input("please enter the additional diet for rohan:\n")
        time = str(getdate())
        ff1.write(f"({d2}+[+{time}+]+\n")
        ff1.close()
    elif n1==2 and n2==3:
        ff2 = open("hammadDiet.txt", "a")
        d3 = input("please enter the additional diet for rohan:\n")
        time = str(getdate())
        ff2.write(f"({d3}+[+{time}+]+\n")
        ff2.close()
    else:
        print("invalid details!")
if x==2:
    if n1==1 and n2==1:
        l=open("harryEx.txt","r")
        print(l.read())
        l.close()
    elif n1==1 and n2==2:
        l1=open("rohanEx.txt","r")
        print(l1.read())
        l1.close()
    elif(n1==1) and n2==3:
        l2=open("hammadEx.txt","r")
        print(l2.read())
        l2.close()

    elif n1==2 and n2==1:
        k=open("harryDiet.txt","r")
        print(k.read())
        k.close()
    elif n1==2 and n2==2:
        k1=open("rohanDiet.txt","r")
        print(k1.read())
        k1.close()
    elif n1==2 and n2==3:
        k2=open("hammadDiet.txt","r")
        print(k2.read())
        k2.close()

    else:
        print("invalid details")







