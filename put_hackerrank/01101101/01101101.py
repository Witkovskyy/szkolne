letter = input().strip().split()
word = ""
for i in letter:
    word = word + chr(int(i, 2))

print(word)