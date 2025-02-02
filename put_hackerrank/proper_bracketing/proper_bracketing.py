line = input()
tab = []
is_true = 1
if len(line)%2==1 or len(line)<=1:
    is_true=0
else:
    for char in line:
        if char == "{" or char == "(" or char=="[":
            tab.append(char)
        else:
            if len(tab)>0:
                temp = tab.pop()
                match char:
                    case "}":
                        if "{" != temp:
                            is_true = 0
                            break
                    case ")":
                        if "(" != temp:
                            is_true = 0
                            break
                    case "]":
                        if "[" != temp:
                            is_true = 0
                            break
                    case _:
                        continue
            else:
               is_true=0 
if len(tab)==0 and is_true==1:
    print("True")
else:
    print("False")
