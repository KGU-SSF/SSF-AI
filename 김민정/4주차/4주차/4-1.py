n=int(input())
for i in range (1, n + 1):
    spaces = " " * (n- i)
    stars ="*" *i
    print(spaces+stars)