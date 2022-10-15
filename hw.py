try:
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{j} * {i} = {i * j}', end="\t")
        print("\n")
except Exception as ex:
   print(f'Erorr information: {ex}')