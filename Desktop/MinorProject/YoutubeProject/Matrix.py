import time
#input nxn matrix
n = int(input())
mat= [list(map(int,input().split())) for _ in range(n)]
for col in mat:
 print(*col)
 time.sleep(1)#wait for 1-sec before printing next row.
 #This will print each row of the matrix one by one,with 1-second delay between each row.
 #print(col[1]) #or
 #print(" ".join(map(str,row)))
print("---print row-----") 
for row in mat:
    for ele in row:
        print(ele)


