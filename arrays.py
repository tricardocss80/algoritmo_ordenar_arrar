def order_list(list):
    longth = len(list) - 1
    for i in range(0, longth):
        print(f'pasada #{i + 1}')
        for j in range(0, longth):
            if list[j] > list[j + 1]:
                aux = list[j]
                list[j] = list[j + 1]
                list[j + 1] = aux
    return list


array = [6, 1, 0, 4, 2, 3, 5, 10, 7, 9, 8]

print('Antes de ordenar')
print(array)
print('Despues de ordenar')
print(order_list(array))
