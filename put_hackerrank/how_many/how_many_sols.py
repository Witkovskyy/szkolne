# xa2 +yb2 = xc2 + yd2

n, x, y = list(map(int,input().strip().split()))
solutions = 0
left_side = []
for a in range(0, n+1):
     for b in range(0, n+1):
          temp_dict = {"a":a, "b":b, "c":a, "d":b}
          if temp_dict not in left_side:
            left_side.append(temp_dict)
            solutions = solutions + 1
            temp_dict = {"a":a, "b":b, "c":b, "d":a}
          if temp_dict not in left_side:
            solutions = solutions + 1
            left_side.append(temp_dict)
          # temp_dict = {"a":b, "b":a, "c":a, "d":b}
          # if temp_dict not in left_side:
          #   left_side.append(temp_dict)
          #   solutions = solutions + 1
          # temp_dict = {"a":b, "b":a, "c":b, "d":a}
          # if temp_dict not in left_side:
          #   solutions = solutions + 1
          #   left_side.append(temp_dict)
            
# for c in range(0, n+1):
#     for d in range(0, n+1):
#          val = (x*(c*c) + y*(d*d))
#          if val in left_side:
#               solutions = solutions + 1

#                 # print(a, b, c, d)
#                 if (x*(a*a) + y*(b*b)) == (x*(c*c) + y*(d*d)):
#                     solutions = solutions + 1
print(solutions)
# print(left_side)
