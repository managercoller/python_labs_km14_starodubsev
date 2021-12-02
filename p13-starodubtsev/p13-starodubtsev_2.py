import os

file_list = os.listdir('archive')

males = dict()
females = dict()

def max_from_file(path):
    names = []
    with open('archive\\'+ path, 'r') as file:
        data = [i.replace('\n', '') for i in file.readlines()]
        for i in data:
            (n,s,o) = i.split(',')
            names.append((n,s,int(o)))
    return max(filter(lambda a: a[1] == 'M', names), key = lambda a: a[2])[0], \
           max(filter(lambda a: a[1] == 'F', names), key = lambda a: a[2])[0]


for path in file_list:
    m, f = max_from_file(path)
    if m in males.keys():
        males[m] += 1
    else:
        males[m] = 1

    if f in females.keys():
        females[f] += 1
    else:
        females[f] = 1

sorted_males = sorted(males.items(), key=lambda a: a[1], reverse=True)

sorted_females = sorted(females.items(), key=lambda a: a[1], reverse=True)
for name, occurrences in sorted_males:
    print(f'{name} {occurrences}')
    print("")
print("")
print("***")
print("")
for name, occurrences in sorted_females:
    print(f'{name} {occurrences}')
    print("")
