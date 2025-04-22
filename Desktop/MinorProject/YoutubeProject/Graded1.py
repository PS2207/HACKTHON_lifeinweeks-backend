def mystery_sort(arr):
    for i in range(len(arr)): #i=0,1,2,3,4 respectively
      for j in range(len(arr) - i -1): #i=0,j=4 | i=1, j=3 |i=2,j=2 |i=3,j=1 |i=4, j=0
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr           
print(mystery_sort([4,2,9,1,6]))#[1,2,4,6,9]

stack=[]
stack.append(5)
stack.append(10)
stack.append(15)
print(stack)#[5, 10, 15]
print(stack.pop(), stack.pop())#15 10  (Last-In-First-Out)

def func(stack):
    stack.append(20)
    stack.pop()
    return len(stack) #3
s= [5,10,15]
print(func(s))

'''
#Which operation takes O(1) time in both a stack and a queue?
Insertion Deletion Searching Both Insertion Deletion
How to convert an array to stack?
how we can use stack to solve some implementation?
(Q)Given a string S=x1,x2,x3...xn output the reverse of S using stack.
input a,b,c,d,e,f  ouput:f,e,d,c,b,a 
for i in range(0,n-1):
    if(p[i]=="("):
      push(s,p[i])
    else:
        if(stack is empty):
            return False
        else:
            pop(s)
    if(stack is empty):
       return True        
    
push(s,a)
push(s,b)
push(s,c)
push(s,d)
push(s,e)
push(s,f)
pop(s)=f 
pop(e)=
(Q)Given a string of paranthesis,check if it properly nested.
Input:(() ()) Output:True
#Input: ())(() Output:False
          
scan from left to right
find left n right next to left then push remove this part
'''         
           
           
           
           
           
           
           
           
           
           



   


