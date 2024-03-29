# 2번

strings = input("입력: ")
tmp_str = ""

for i in range(len(strings)):
    if strings[i] == "[":
        tmp_str = strings[i + 1: len(strings) - 1]
        break

tmp_li = tmp_str.split(", ")

for data in tmp_li:
    print(data)
    