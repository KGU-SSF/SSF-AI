num = list(map(int,input().split()))
cnt = num.count(0)
result = {0:"D",1:"A",2:"B",3:"C",4:"E"}
print(result.get(cnt))