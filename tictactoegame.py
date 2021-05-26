from IPython.display import clear_output
l1=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
l5=[['a','b','c'],['d','e','f'],['g','h','i']]

def refresh():
    l1=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    l5=[['a','b','c'],['d','e','f'],['g','h','i']]
def putinfo(pos,value):
    if(pos==7):
        l1[0][0]=value
        l5[0][0]=value
    elif(pos==8):
        l1[0][1]=value
        l5[0][1]=value
    elif(pos==9):
        l1[0][2]=value
        l5[0][2]=value
    elif(pos==4):
        l1[1][0]=value
        l5[1][0]=value
    elif(pos==5):
        l1[1][1]=value
        l5[1][1]=value
    elif(pos==6):
        l1[1][2]=value
        l5[1][2]=value
    elif(pos==1):
        l1[2][0]=value
        l5[2][0]=value
    elif(pos==2):
        l1[2][1]=value
        l5[2][1]=value
    else:
        l1[2][2]=value
        l5[2][2]=value
def display(c):
    if(c==1):
        clear_output()
    print(f' {l1[0][0]} | {l1[0][1]} | {l1[0][2]}')
    print("-----------")
    print(f' {l1[1][0]} | {l1[1][1]} | {l1[1][2]}')
    print("-----------")
    print(f' {l1[2][0]} | {l1[2][1]} | {l1[2][2]}')
ch='y'
while(ch=='y' or ch=='Y'):
    refresh()
    count=0
    f=0
    pos=0
    lc=[]
    for i in range(0,50):
        val='b'
        while val not in ['x','o','X','O']:
            val=input("\nenter x or o : ")
            print(" ")
            if val not in ['x','o']:
                print("enter x or o properly ")
            c=1
            position=0
        while(position not in range(1,10)):
            print("7 | 8 | 9\n----------\n4 | 5 | 6\n----------\n1 | 2 | 3")
            position=int(input("Enter the position as shown: "))
            if(f!=0 and position in lc):
                print("Position already filled, Enter a different one ")
                c=0
                display(c)
            lc.append(position)
            f+=1
            print(" ")
            
            if(position not in range(1,10)):
                print("Invalid position, Enter again ")
        if(c!=0):
            putinfo(position,val)
            display(c)
            for i in range(0,3):
                if(l5[i][0]==l5[i][1] and l5[i][0]==l5[i][2]):
                    count=1
                    if count==1:
                        print(f' \n {l5[i][0]} is the winner' )

            for i in range(0,3):
                if(l5[0][i]==l5[1][i] and l5[0][i]==l5[2][i]):
                    count=1
                    if count==1:
                        print(f' \n {l5[0][i]} is the winner' ) 

            if ((l5[0][0]==l5[1][1] and l5[0][0]==l5[2][2]) or (l5[0][2]==l5[1][1] and l5[0][2]==l5[2][0])):
                count=1
                print(f' \n {l5[1][1]} is the winner' )        
            if count==1:
                ch=input("\n do u wanna play again y/n ")
                l1=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                l5=[['a','b','c'],['d','e','f'],['g','h','i']]
                break
