mno1 =(input("Input the phrase number 1: ")).lower()
mno2 =(input("Input the phrase number 2: ")).lower()



mno12= set()
mno22= set()



for i in mno1:

    if i.isalpha() ==True:

        mno12.add(i)
for i in mno2:

    if i.isalpha() ==True:

        mno22.add(i)


print(mno12)
print(mno22)


if mno12 & mno22==mno22:

    print("first phrase has all letters from second phrase")
   
else:

    print("first phrase hasn't all letters from second phrase")

