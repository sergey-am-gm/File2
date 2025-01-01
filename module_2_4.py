numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for k in  range (2, numbers[i]): # для numbers[i] = 2 цикл не выполняется, что есть правильно,
                                     # при этом is_prime = True, число простое, хотя и чётное.
        if numbers[i] % k == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not Primes: ',not_primes)




