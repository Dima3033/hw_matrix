try:
    start = int(input('Enter num ->'))
    end = int(input('Enter num ->'))
    counter = 0
    for i in range(start, end + 1):
        counter = 0
        if i == 1:
            print(i, ' ')
            continue
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            print(i, '\t', end="")
except Exception as ex:
   print(f'Erorr information: {ex}')