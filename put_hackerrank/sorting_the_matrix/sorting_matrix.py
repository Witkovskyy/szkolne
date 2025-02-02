n,m = map(int,input().strip().split())
unsorted_m = []
for i in range(n):
    temp_arr = (list(map(int,input().split())))
    for j in range(len(temp_arr)):
        unsorted_m.append(temp_arr[j])
unsorted_m.sort()
sorted_m = []
for i in range(n):
    temp_arr = []
    for j in range(i,len(unsorted_m),n):
        temp_arr.append(unsorted_m[j])
    sorted_m.append(temp_arr)
for i in range(n):
    for j in range(m):
        print(sorted_m[i][j], end=" ")
    print()


