#initial state
jug1,jug2=4,3
x,y=0,0
def filljug1(x,y):
    return (4,y)

def filljug2(x,y):
    return x,3
 
def pourjug1tojug2(x,y):
    if( y == jug2 ):
        print("Jug 2 is already full!")
        return (x,y)
    elif( (x == 0) ):
        print("Jug 1 is empty")
        return (x,y)
    else:
        remain = (3-y)
        if(remain > x):
            y += x
            x = 0
        else:
            x -= remain
            y += remain
    
def emptyjug1(x,y):
    return(0,y)
    
def emptyjug2(x,y):
    return(x,0)
def pourjug2tojug1(x,y):
    if( x == jug1 ):
        print("Jug 1 is already full!")
        return (x,y)
    elif( (y == 0) ):
        print("Jug 2 is empty")
        return (x,y)
    else:
        remain = (4-x)
        if(remain > y): #4 > 3
            x += y
            y = 0
        else:
            y -= remain
            x += remain
        return (x,y)

           
print("These are your choices: ")
print("1.fillJug1 2.fillJug2 3.pourFromJug1toJug2 4.pourFromJug2toJug1 5. empty jug1 6.empty jug2 7.Exit :")

print(x,y)
while(True):
    choice = int(input())
    if(choice == 1):
        x,y = filljug1(x,y)
        print(x,y)
    elif(choice == 2):
        x,y = filljug2(x,y)
        print(x,y)
    elif(choice == 3):
        x,y =pourjug1tojug2(x,y)
        print(x,y)
    elif(choice == 4):
        x,y = pourjug2tojug1(x,y)
        print(x,y)
    elif(choice == 5):
        x,y = emptyjug1(x,y)
        print(x,y)
    elif(choice == 6):
        x,y = emptyjug2(x,y)
        print(x,y)
    elif(choice == 7): break
    else:
        print("Invalid Choice!")
   
           