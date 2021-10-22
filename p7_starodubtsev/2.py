a=True
numinsix=""
for i in range(0,3):
    while a:
        m = input("Введить значення ")
        
        
        if m.isdigit()==True and len(m)<=3:
            a = False
            if len(m)==1:
                m="0"+m
                numinsix = numinsix+m
            
            elif len(m)>=2:
                if float(m)/16>=1:
                    full = int(m)//16
                    ntfull=int(m)- full*16
                    if full ==15:
                        numinsix=numinsix+"F"
                    elif full == 14:
                        numinsix =numinsix+ "E"
                    elif full == 13:
                        numinsix = numinsix+"D"
                    elif full == 12:
                        numinsix =numinsix+ "C"
                    elif full == 11:
                        numinsix =numinsix+ "B"
                    elif full == 10:
                        numinsix =numinsix+ "A"
                    else:
                        numinsix=numinsix+str(full)


                    
                    if ntfull ==15:
                        numinsix=numinsix+"F"
                    elif ntfull == 14:
                        numinsix =numinsix+ "E"
                    elif ntfull == 13:
                        numinsix = numinsix+"D"
                    elif ntfull == 12:
                        numinsix =numinsix+ "C"
                    elif ntfull == 11:
                        numinsix =numinsix+ "B"
                    elif ntfull == 10:
                        numinsix =numinsix+ "A"
                    else:
                        numinsix=numinsix+ str(ntfull)
                else:
                    numinsix = numinsix+"0"
                    if int(m) ==15:
                        numinsix=numinsix+"F"
                    elif int(m) == 14:
                        numinsix =numinsix+ "E"
                    elif int(m) == 13:
                        numinsix = numinsix+"D"
                    elif int(m) == 12:
                        numinsix =numinsix+ "C"
                    elif int(m) == 11:
                        numinsix =numinsix+ "B"
                    elif int(m) == 10:
                        numinsix =numinsix+ "A"                        
        else:
            print("Число было введено некорректно.\nПопробуйте еще раз") 
    a=True   
print(numinsix)