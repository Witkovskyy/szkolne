def palindrome(to_check, length):
    for i in range(length-1,-1,-1):
        if to_check[i]=='0':
            if len(to_check)<1: return False
            to_check = to_check[:-1]
        else:
            if to_check==to_check[::-1]:
                return True
            else:
                return False
        if len(to_check)<1: return False



line = input()
sum = 0
for i in range(len(line)):
    for j in range(len(line)):
        to_check = line[j:j+i+1]
        if len(to_check)<(i+1):
            continue
        else:
            is_palindome = palindrome(to_check,(i+1))
        if is_palindome:
            sum +=1
print(sum)