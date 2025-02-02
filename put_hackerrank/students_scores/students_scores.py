students,tests_dict, appearances = {},{},{}
tests = []
amount = int(input())
for line in range(0, amount):
    line = input()
    key, value = line.strip().split(" ", 1)
    students[key] = value
for key in students:
    temp = (students[key].split(" ")) 
    for item in temp:
        tests.append(item)
for item in tests:
    key, value = item.strip().split(":")
    if key not in tests_dict:
        tests_dict[key] = float(value)
    else:
        tests_dict[key] += float(value)

    if key not in appearances:
        appearances[key] = 1
    else:
        appearances[key] += 1
for key in tests_dict:
    tests_dict[key] = tests_dict[key]/appearances[key]
sorted_tests = dict(sorted(tests_dict.items()))
sorted_studs = dict(sorted(students.items()))
for key in sorted_studs:
    avg = 0
    temp_sum = 0
    iterator = 0
    values = sorted_studs[key].split(" ")
    for item in values:
        char = ":"
        temp = float(item.split(char)[-1])
        temp_sum += temp
        iterator +=1
    avg = temp_sum/iterator
    sorted_studs[key] = avg
for key in sorted_studs:
    print(f"{key} {sorted_studs[key]}")
for key in sorted_tests:
    print(f"{key} {sorted_tests[key]}")