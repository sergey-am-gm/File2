first = int(input('введите первое число: ',))
second = int(input('введите второе число: ',))
third = int(input('введите третье число: ',))
if first == second == third:# попарно сравнивает, результаты объединяет по 'AND'
    print(3)
elif first != second != third != first:# все не равны
    print(0)
else: print(2)


