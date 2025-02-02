n = int(input())
table = list(map(int, input().split()))

sublists = []
biggest_sum = float('-inf')
#get al sublists
for i in range(n):
    for j in range(n):
        part = table[i : j + 1]
        if len(part) > 0:
            sublists.append(part)

for sublist2 in sublists:
    suma2 = 0
    for i in range(0, len(sublist2), 2):
        suma2 += sublist2[i]
    for sublist3 in sublists:
        suma3 = 0
        for i in range(0, len(sublist3), 3):
            suma3 += sublist3[i]
        
        if suma2==suma3 and suma2 > biggest_sum:
            biggest_sum = suma2
            # print(suma2)
        
print(biggest_sum)
