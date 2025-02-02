def prime(to_check, lenght):
    for i in range(2,to_check):
        if to_check%i==0:
            return False
    return True

line = input()
primes = []
for i in range(len(line)):
    for j in range(len(line)):
        to_check = line[j:j+i+1]
        if len(to_check)<(i+1) or int(to_check)==0:
            continue
        else:
            to_check = int(to_check)
            is_prime = prime(to_check, (i+1))
        if is_prime and to_check not in primes and to_check!=1:
            primes.append(to_check)
for i in range(len(primes)):
    primes[i] = str(primes[i])
primes = sorted(primes, reverse=True)
for item in primes:
    print(item)
            