
song = ["Deen Assalam Lyrics Sabyan Gambu","Beautiful In White Lyrics Westlife","In My Feelings Lyrics Drake","High Rated Gabru Lyrics Guru Randhawa","Mercy Lyrics Brett Young","Despacito Lyrics Luis Fonsi","Shree Hanuman Chalisa Lyrics Hariharan","Daru Badnaam Lyrics Param Singh","Mile Ho Tum Lyrics Tony Kakkar","Torete Lyrics Moonstar88"]
year = ["1991","1992","1993","1990", "1994","1995","1996", "1997","1998","1999"]


song1=[]


for i in range(0,10):
    song1.append({"Composition":song[i],"Year":year[i]})


import csv

with open('sample.csv',"w", newline='') as csvfile:
    fieldnames=["Composition","Year"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames )
    writer.writeheader()
    writer.writerows(song1)
print('Starting to read csv file')

with open('sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(*row, sep=', ')
print('Done Reading')
    