def reverse(a):
    rev_str = []
    for i in a[::-1]:
        rev_str.append(i)
    return rev_str

origin = list(input())
rev = reverse(origin)

print(origin == rev)