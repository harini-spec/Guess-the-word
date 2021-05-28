import random
chance=5
count=0
genre=["sports person","food","country"]
print("genres:\n","1.",genre[0],"\n2.",genre[1],"\n3.",genre[2])
choice=int(input("Enter choice number"))
sports=["nadia comaneci","pele","sebastian vettel","charles leclerc","robert james fischer","floyd mayweather"]
food=["bruschetta","quinoa","edamame","tzatziki","charcuterie","bourguignon"]
country=["belarus","papua new guinea","guadeloupe","mozambique","liechtenstein","cambodia"]
if(choice==1):
    question=random.choice(sports)
elif(choice==2):
    question=random.choice(food)
else:
    question=random.choice(country)
question.upper()
for i in question:
    if(i==" "):
        print("   ",end=" ")
    else:
        print("_",end=" ")
guess=""
while(chance>0):
    fail=0
    ch=input("\n\nEnter any character:")
    guess+=ch
    for char in question:
        if char in guess:
            print(char,end=" ")
        elif (char==" "):
            print(" ",end=" ")
        else:
            print("_",end=" ")
            fail+=1

    if(fail==0):
       print("\n\nYou win")
       break
            
    if ch not in question:
        print("\n",end="")
        print("*    *")
        print("  *  ")
        print("*    *")
        chance-=1
        print(chance,"chances left",end="")
if(chance==0):
    print("\n\nYou lose")
    
