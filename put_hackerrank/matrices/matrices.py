n = int(input())
first_matrix, second_matrix = [], []
for i in range(n):
    first_matrix.append(input().strip().split())
for i in range(n-1):
    second_matrix.append(input().strip().split())
for i in range(n*n):
    test_matrix = [[0]*(n-1)]*(n-1)


    # print(test_matrix) 
    # print()


    