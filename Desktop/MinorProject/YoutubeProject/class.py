#The Python function calculates the factorial of a given number using recursion.
def fact(n):   #defining function named (fact) that takes one argument n
   #Base case: the condition that stops further resursive calls.
    if n == 0 or n == 1:
        return 1  #factorial =1
    else:
        #Recursive case: the part of the function 
        
        return n * fact(n - 1) # 5 * fact(4)

print(fact(5)) 
#-----------------------------------
#Fibonacci number- 1,1,2,3,5,8,13
def fib(n):
    if n==1:
        return (1)
    if n==2:
        return 1
    else return fib(n-1) + fib(n-2)
#------------------------------------
Input:  Two Sorted arrays A and B of size not
Output: One single sorted array of size 2n   

#------------------------------------
n, q = map(int, input().split())
print(n,q)
arr = set(map(int, input().split()))  # Using a set for fast lookup
#print(arr)
for _ in range(q):
    x = int(input())
    print("Yes" if x in arr else "No")
n, q = map(int, input().split())
arr = set(map(int, input().split()))  # Using a set for fast lookup

for _ in range(q):
    x = int(input())
    print("YES" if x in arr else "NO")
    
'''    
    if x in arr:
        print("YES")
       
    else:
        print("NO") 
'''        
'''       
input:
3 2
2 4 5
2
YES(output)
3
NO(output)
but i want like this
input :
3 2
2 4 5
2
3
output
YES
NO    
'''        
# Read input in one line and convert to list of string or integers
arr=list(map(str,input().split()) )    # ['2', '3', '4']
#arr=list(map(int,input().split()))   # [2, 3, 4] 
print(arr) 
#-------------------
n = int(input())  # Read number of elements to insert in array
arr = []  # Initialize an empty list
for i in range(n):
    arr.append(int(input()))  # Append input to list
print(arr)
print(type(arr))  # Print the entire list [2, 3, 4] # <class 'list>
#print(*arr) # 2 3 4
print(",".join(map(str, arr))) # 2,3,4

#Using sys.stdin.read() for Large Inputs
import sys
n = int(input())
arr= list(map(int, sys.stdin.read().split()))


'''
import heapq

heap= [3, 1, 4,2, 1, 5] # list
#convert list into min heap/priority queue keeps smallest element at the top,, we can peek using heap[0]
queue = heapq.heapify(heap) #None 
smallest_element=heap[0]  # Peek without removing
print(smallest_element)   # Output: 1


def next_greater_element(arr):
    n=len(arr)
    result=[-1]*n #initialize all elements with -1
    stack=[]      #stack to store indices of elements
    for i in range(n):  #Maintain decreasing order in the stack
        while stack and arr[i] > arr[stack[-1]]:
            index=stack.pop()
            result[index]=arr[i]  #Assign next greater element
        stack.append(i)           #Push current index onto the stack
    return result
arr=[4,5,2,10,8]
print("Next Greater Element: ",next_greater_element(arr))#Next Greater Element:  [5, 10, 10, -1, -1]
#why we take worst case?

#Try to implement queue using 2 stack
'''