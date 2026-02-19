#code for simple repeating calculator untill user exits
print("\tWELCOME!!\t")
while True:
    
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Square\n7.EXIT!")
    
    choice = int(input("Enter your choice :"))
    
    if(choice==7):
        print("Exiting the calculator. Goodbye!")
        break
    else:
        a = float(input("Enter value of a:"))
        b = float(input("Enter the value of b:"))
            
        if(choice==1):
            print("Additon=",a+b)
        elif(choice==2):
            print("Subtraction=",a-b)
        elif(choice==3):
            print("Multiplication=",a*b)
        elif(choice==4):
                if(b==0):
                    print("Division can't be perfom ")
                else:
                   print("Division=",a/b)
        elif(choice==5):
             if(b==0):
                    print("Modulo operation can't be perfom ")
             else:
                print("Modulo i.e remainnder of division",a%b)
        elif(choice==6):
            print("Square of a = ",a**2)
            print("Square of b = ",b**2)
        else:
            print("Enter valid choice!!")
