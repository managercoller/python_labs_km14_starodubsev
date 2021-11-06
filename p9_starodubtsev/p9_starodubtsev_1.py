
import numpy as np
import itertools
q = True
while q :
    a = input("Enter a number of rows and columbs, more than 0:")
    if a.isdigit():
        if int(a)>0:
          q=False
          num=int(a)
        else:
            print("You haven't entered right number")
    else:
        print("You haven't entered right number")
ind = []
mnosh = []
for i in range(0,num):
    ind.append(i)
new = list(itertools.permutations(ind,num))
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix
matrix = random_matrix(num)
index = []
permetush = []
def permutation():
    #Робимо растановку
    helper = []
    factorial = 1
    for i in range(0, num):
        index.append(i)
        if(i!=0):
            factorial=factorial*i
    factorial =factorial*num
    for i in range(0,factorial):
        for j in range(0, num):
            helper.extend([matrix[j][new[i][j]]])
        permetush.append(helper)
        helper=[]
def dodatki():
    #Знаходженння добутків всіх елементів
    for paper in permetush:
        n=1
        for i in paper:
            n=n*i
        mnosh.append(n)
def pokaznik():
    #Це наша відповідь та сума
    n2 , n3 =  0,0
    for paperic in new:
        n1 = 0
        for i in range(0, num):
            for j in range(i+1, num):
                if paperic[i]>paperic[j]:
                    n1 += 1
        if n1%2==0:
            n2 = n2+mnosh[n3]
        else:
            n2 = n2-mnosh[n3]
        n3 += 1
    return n2
permutation()
dodatki()
print("it is ",str(pokaznik()))
print("of")
print(matrix)
