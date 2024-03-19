nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = list(map(int, nums))

odd = [x for x in number if x % 2 != 0]

print(odd)



'''nums = list(map(int, input("숫자를 입력하세요.\n").split()))

odd = [x for x in nums if x % 2 !=0]
odd.sort()

print(odd)'''