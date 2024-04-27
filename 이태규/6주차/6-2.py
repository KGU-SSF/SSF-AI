q = []                  
k = int(input())        

for i in range(0,k):    
    qu = int(input())   
    if(qu!=0):          
        q.append(qu)    
    else :
        q.pop()         

result = sum(q)         
print(result)