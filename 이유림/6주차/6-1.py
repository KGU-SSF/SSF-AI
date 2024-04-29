word = input()

a = True
for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        a = False
        break

print(a)