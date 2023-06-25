def find_prime_factors(number):
    ls=[]
    deli=2
    while deli<=number:
        if number % deli == 0:
            ls.append(deli)
            number = number // 2
        else:
            deli +=1
    return ls
test = find_prime_factors(99)
print(test)