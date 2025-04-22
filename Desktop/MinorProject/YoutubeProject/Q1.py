'''
def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the number of elements in the array
        arr = list(map(int, input().split()))  # Read the array of integers
        print(arr)  # (Optional) Print to check if input is read correctly

main()
'''
def recursive_sum(arr, n):
 #this prevents further recursion & provide a stopping conditions
    if n == 0:
      return 0
    return arr[n - 1] + recursive_sum(arr, n - 1)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        #arr = list(map(int, input().split()))[:n]
        while True:
          arr= list(map(int,  input().split() ))
          if len(arr)==n :
            break
        print(recursive_sum(arr, n))

if __name__ == "__main__":
    main()

from collections import deque
queue= deque() # create queue
queue.append(1)
print(queue)


stack=[]
n=100
i=-1
def push(x):
    if(len(stack)==n):
        print("overflow")
    else: 
        stack.append(x)
def pop(x):
    if(len(stack)==0): 
        print("underflow")
    else:
        print(stack[-1])
        stack.pop()
def empty():
    if(len(stack)==0): 
      return True  
def full():
    if(len(stack)==n):
        return True
def top():
    if(len(stack)!=0):
        return stack[-1]
    
#______________________________________
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr
arr=[64,25,12,22,11]
sorted_arr=selection_sort(arr)
print("Sorted array: ",sorted_arr)
#_________________________________________ 
'''   
def bubbleSort(arr[],n):
    
    for(i=0;i<n-1;i--):
        swapped=false    
        for(j=0;j<=n-1;j++):
          if(arr[j] > arr[j+1])
            swap(arr[j], arr[j+1]);
            swapped=true
          
        
        if(swapped==false):
          break;
''' 
def modulo_sort(n, k, arr):
    # Sorting based on modulo k while maintaining stable order for equal mod values
    sorted_arr = sorted(arr, key=lambda x: (x % k))
    
    # Printing the sorted array
    print(*sorted_arr)
    #print(" ".join(map(str, sorted_arr)))

# Example usage
n = 5
k = 6
arr = [12, 18, 17, 65, 46]
modulo_sort(n, k, arr)

def modulo_sort(n, k, arr):#n = no of elements in array, k=n divided by k
   
    # Sorting the array based on (element % k) while maintaining stability
    #arr.sort(key=lambda x: (x % k)) #both can use
    new_arr=sorted(arr,key=lambda x: (x % k))
    print(*new_arr)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# Reading input
'''
This modifies original list ,doesn't return a new list ,returns None
This doesn't modify original list, returns new sorted list
'''

# Calling the function
modulo_sort(n, k, arr)
#__________________
'''
Input:
5 6
12 18 17 65 46
Output:
12 18 46 17 65 
'''
#___________________
'''
n x n matrix
Input Sample if:
5
12345
67891
23456
78912
34567
Output Sample if:
93
Boundry elements-1,2,3,4,5, 1,6,2,7, 6,5,4,3, 7,2,6
Diagonal elements(without counting an element twice)- 7,4,1,9,4,8

#For Diagonal elements:-
for i in range(0,n-1):
    if (v[i]==0):
        sum = sum+ matrix[i][i]
        
'''
         
                    
    






















