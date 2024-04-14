N = int(input())  
for i in range(1, N + 1):
    result = ""
    result += " " * (N - i)  
    result += "* " * i  
    print(result)   