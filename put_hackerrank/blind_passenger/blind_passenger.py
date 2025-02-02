t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print("poor conductor")
    else:
        row = (n - 2) // 5 + 1
        new_n = n
        if row%2!=0:
            temp_num = new_n%10
            if temp_num==2:
                direction = "L"
                pos = "W"
            elif temp_num==3:
                direction = "L"
                pos = "A"
            elif temp_num==4:
                direction = "R"
                pos = "A"
            elif temp_num==5:
                direction = "R"
                pos = "M"
            else:
                direction = "R"
                pos = "W"
        else:
            temp_num = new_n%10
            if temp_num==1:
                direction = "L"
                pos = "W"
            elif temp_num==0:
                direction = "L"
                pos = "A"
            elif temp_num==9:
                direction = "R"
                pos = "A"
            elif temp_num==8:
                direction = "R"
                pos = "M"
            else:
                direction = "R"
                pos = "W"

        print(f"{row} {pos} {direction}")