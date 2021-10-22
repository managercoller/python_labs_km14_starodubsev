format_tuple = (37.863, 'Brent', 3, 62.887, 1, 11)
print("The price of {0[1]} crude oil fell to $ {1} per barrel, setting a {0[2]}-month anti-record. The current price is only {3} of last year's {0[1]} oil price on the same day {2}.{0[5]}.".format(format_tuple, round(format_tuple[0],2), str(format_tuple[4]).zfill(2),round(format_tuple[3],2)))

