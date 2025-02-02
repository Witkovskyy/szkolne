n = int(input())
weights = input().strip().split()
for i in range(0, n):
    weights[i] = int(weights[i])
total_sum = sum(weights)
min_sum_diff = float('inf')
former_sum = 0
for t in range(0, n):
    former_sum = former_sum + weights[t]
    s1 = former_sum
    s2 = total_sum - former_sum
    temp_sum_diff = abs(s1-s2)
    min_sum_diff = min(min_sum_diff, temp_sum_diff)
 
print(min_sum_diff)
