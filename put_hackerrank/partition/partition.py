length_of_table = int(input())
big_list = list(map(int,input().strip().split()))
biggest_sum = float('-inf')
b_sums = []
for third_loop_iterator in range(0,length_of_table):
        temp_sum_b = 0
        for fourth_loop_iterator in range(third_loop_iterator,length_of_table,3):       
            temp_sum_b += big_list[fourth_loop_iterator]
            if temp_sum_b not in b_sums:
                b_sums.append(temp_sum_b)

for biggest_loop_iterator in range(0,length_of_table):
    temp_sum_a = 0
    for second_loop_iterator in range(biggest_loop_iterator,length_of_table,2):
        temp_sum_a += big_list[second_loop_iterator]
        # print(f"{temp_sum_a} {temp_sum_b}")
        if temp_sum_a in b_sums:
            if temp_sum_a>biggest_sum:
                biggest_sum = temp_sum_a
print(biggest_sum)