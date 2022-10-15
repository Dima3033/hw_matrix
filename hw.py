n1 = int(input(' число 1 '))
n2 = int(input(' число 2 '))
for i in range(1, 11):
    for j in range(n1, n2+1):
        print(f'{j} * {i} = {i * j}', end="\t")
    print("")