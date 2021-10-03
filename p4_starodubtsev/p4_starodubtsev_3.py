while check:

    year = float(input("Input the number of years: "))


    if year < 0:
        print("You have enter number that is less than zero. Try againg.")


    elif year>2:
        year_dog = 10.5*2+(year-2)*4
        print("In dog's year it is:", year_dog)
        check = False


    else:
        year_dog = year *10.5
        print("In dog's year it is:", year_dog)
        check = False