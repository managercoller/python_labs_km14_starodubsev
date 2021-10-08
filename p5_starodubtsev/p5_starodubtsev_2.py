list_of_goods = []
n = int(input("Input the number of the words: "))
for i in range(0,n):
    w = input("Input the word: ")
    list_of_goods.append(w)
    
list_of_goods[n-1] = "and "+list_of_goods[n-1]
if n>2:
    for i in range(0,n-1):
        list_of_goods[i] = list_of_goods[i]+","

for i in range(0,n):
    print(list_of_goods[i], end="")