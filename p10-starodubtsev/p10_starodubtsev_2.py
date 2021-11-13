import numpy as np

years = np.arange(1900, 2020+1, 1)
months = {
    '1':31,
    '2':28,
    '2*':29,
    '3':31,
    '4':30,
    '5':31,
    '6':30,
    '7':31,
    '8':31,
    '9':30,
    '10':31,
    '11':30,
    '12':31
}

def intercalary(lst):
    lst1 = list(filter(lambda x: x % 400 == 0 or (x%100!=0 and x%4==0), lst))
    return lst1


def days(func, m, y):
    new_list = func(years)
    if int(y) in new_list:
        if m=='2':
            m='2*'
    return months.get(m)

a = True
while a:
    month = input('input the number of the month: ')
    year = input('input the number of the year: ')
    if month.isdigit() and year.isdigit():
        if 0<int(month)<13 and len(year)==4:
            a = False
        else:
            print('incorreсt input. try again...')
    else:
        print('not all character in string are digits. try again...')
print(days(intercalary, month, year))