km_h = float(input("Please input speed: "))


if km_h<137:

    print("Minor")
elif km_h<0:
    print("You have entered number with minus")

elif 177>=km_h>137:

    print("Moderate")

elif 217>=km_h>177:

    print("Considerable")

elif 266>=km_h>217:

    print("Severe")

elif 322>=km_h>266:

    print("Devastating")

else: 

    print("Incredible")
