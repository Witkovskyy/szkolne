n = int(input())
heights = input().strip().split()
for i in range(0, n):
    heights[i] = int(heights[i])
max_sum = 0
for i in range(0, n-1):
    temp_sum = 0
    for j in range(i, n-1):
        if heights[j]<heights[j+1]:
            break
        else:
            temp_sum = temp_sum + 1
    if temp_sum>max_sum:
        max_sum = temp_sum
print(max_sum)