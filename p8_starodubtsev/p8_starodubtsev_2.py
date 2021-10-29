a=True
while a:

    try:
        a = float(input('please input a: '))
        b = float(input('please input b: '))
        c = float(input('please input c: '))
        d = b**2 - 4*a*c
        if d<0:
            raise ValueError("there aren't roots")
        elif a==0:
            raise ValueError("division by zero")
        elif b==0 and c==0:
            raise ValueError("It isn't equation")
        
        elif d ==0:
            
            print("there are only one root")
            x1 = -b/(2*a)
            raise ValueError("It's",x1)
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d**0.5)/(2*a)
        print("x1=",x1,"x2 =",x2)
    except Exception as exp:
        print(exp)
        print('oops')
    x=input("If you wanna stop, please enter y, or if you not, type enter ")
    if x=="y":
        a=False
