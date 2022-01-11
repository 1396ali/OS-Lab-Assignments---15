def pascal(n):
    list=[]
    for i in range(n):
        list.append([1]*(i+1))
        
    for i in range(2,n):  
        for j in range(1,i)  :
            list[i][j]=list[i-1][j-1]+list[i-1][j]
            
    return list
        
num = int(input("Please enter number of depth: "))
inp = pascal(num)
for x in inp:
    print(x)