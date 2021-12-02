import string

data = []

with open('gadsby.txt', 'r') as file:
    data = [*''.join(file.readlines()[114:])]

data = [i.lower() for i in data if i.isalpha()]

count = len(data)

occurrences = dict()
for char in string.ascii_lowercase:
    occurrences[char] = data.count(char)

sorted_occurences = sorted(occurrences.items(), key= lambda a: a[1], reverse = True)

percent = lambda a: (a[1] / count) * 100

for elem in sorted_occurences[:5]:
    print(f'{elem[0]} - {percent(elem):6.3f}%')

print()

for elem in sorted_occurences[-5:]:
    print(f'{elem[0]} - {percent(elem):6.3f}%')