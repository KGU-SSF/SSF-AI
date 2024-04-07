a = []
for i in range(3):
    a.append(input().split())
b=['D','C','B','A','E']
for i in range(3):
    print(b[a[i].count('1')])