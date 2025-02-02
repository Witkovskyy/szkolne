l = list(map(int, input().strip().split()))
k = int(input())
for i in range(k):
    start, end = map(int, input().strip().split())
    print(sum(l[start:end+1]))


