comparison based sort -Bubble,Selection sorting
sorting algorithm: Insertion,Merge,Heap
Problem1:
Given a sorted array, Our goal is to find element x in the array.
Find the middle index,compare the element with it.
If it is less than consider the left half of array,
otherwise consider right half of array.
T(n)=T(n/2)+O(1)
By applying master theorem, T(n) =O(logn)

Problem2:
Given a set of n points on a circle p1,p2,...pn, 
each having coordinates (xi,yi).
The first point is the leftmost point of the circle,and 
the points are arranged in a clockwise order as they appear on the circle.
Find the rightmost point. 
solution:
the value is x is increasing then x is decreasing.

array
[(-5,0),(-3,4),(0,5),(3,4),(5,0),(3,-4),(0,-5),(-3,4)]
[-5 -3 0 3 5 3 0 -3] Find rightmost element   (0+7)/2=3
           * 
(4+7)/2 5   (4+5)/2=4
2 searching algorithm: 1.Linear Serach 2.Binary search
In Linear Search: no need sorted data  
Selected sort Bubble Sort  is T.c(Time Complexity) of selected sort is nsq

In Binary serach- need sorted data
#Pseudo code
LS(A,n,x):
    for i in range(n):
        
        if A[i]=x:
            return i
     return -1   
 T(n) =T(n-1) +c and T(1)= 1
 
We have an algorithm for searching with: 
Time complexity= O(n) 
space complexity = O(1)    

Can we do better?
Means- Can we come up with an algorithm that reduce Sapce & time comlexity:
Can we improve the TC of the propose algorithm?
Answer is Binary Search Algorithm
   
Best case: Represents Minimum time taken by algorithm  to produce output 
x=4
A       

No of comparison=1
Each comparison take 
Thus total time 1.c=O(1)


Worst case: represents maximum time taken by an algorithm to produce 
x=8
check from start to end
4 9 3  1 0 5 2 7 6 8
Number of comparisons are n
Each comparison take constant time, let say c.
Thus total time is n.c=O(n)

Average case: Represents time taken by an algorithm on an average to produce an output
    
1 comparison if x=4
x=9
x=3 and so on  
n comarison if x=8
Total comparison 1+2+3+....next n= n(n+1)/2
(n(n+1)/2)/n = (n+1)/2 =O(n)
    
T(n) is Time taken to search in n-elements
T(n) ----------> value c    
  |
  |
T(n-1) --------> value c 
  |
  | 
T(n-2)  
  |
  |  
T(2)
  |
  |
 T(1) 
    
 
An array A[n] and element x    
Array is sorted means- Increasing or Decreasing order  

i, such that A[i]=x
-1, if A[i]!= x for any i belong to {1,2...n}  
    
search x=89 using binary search
A[11 13 16 18 19 21 29 89 90 99] 

(1st index + last index)/2=  (1+10)/2= 5.5 =5
    
discard all
now search 89 among [21 29 89 90 99]    
    
(6+10)/2 =8 (index)   
    
so return 89

seach x=16
(1+10)/2=5.5 =5
compare 16 to elemnet present at 5 i.e 19 16 is less that 19
so discard insex after 5
(1+4)/2= 2.5 =2
check at index 2 i.e 13
now compare 13 to 16 16 is greater
so discard index before 


BS(A[p,q], x):
    if A[mid_index] = x:
        return x
    if A[mid_index] > x:
        return BS(A[p, mid_index -1 ])
    
    if A[mid_index] < x:  
        return BS(A[mid_index +1 ], q)

Number of comparisons are 1
Each comparison take constant time, lets say c

Best case
search x=19
(1+10)/2=5.5.=5
mid_index=5

Worst case search elements x=18
18<19
so 18 is present before index 5 subarray so (1+4 )/2 =2

no of comparison are 4
How many maximum number of comparison can be made in an array of n elements?


T(n) is Time taken to search in n-elements
T(n) ----------> value c    
  |
  |
T(n-2) --------> value c O(log n) so height c.log(n)
  |
  | 
T(n-2 sq)  
  |
  |  
T(2)
  |
  |--------> value c
 T(1) 
hight of tree- number of elements present here. 
x = A[mid] 
Comparison is same as finding the number in terms in G.P series
n, n/2, n/2sq...1

1=n(1/2 pow n-1)

Average case analysis:
Recurrence Relation:
After analyzing the pseudo code we get,
    T(n) = T((n-1)/2) + c
    
x= 44
mid=(1+6)/2 =3.5.=3  
Consider a simple recurrence
T'(n) = T'(n/2)+c  

Verify that, T(n)<= T'(n)

f(n) = O(g(n))
f(n) <= g(n)

if we solve T'(n) in O-notation


space complexity =O(log n) because of stack size
O(1)

Algorithm       Time Complexity   Space Cpmlexity  Requires Sorted Data
Linear Search       O(n)             O(1)                    No
Binary Search       O(log n)         O(1)                    Yes 


Q)We are given an unsorted data and we need to search an element in it.
Approach1: Apply the Linear search ---->  O(n)
Approach2: Sort the data and then Apply the Binary search

Which approach is better and why? Ans: approach is better in terms of time comlexity.
O(n.log n) + O(log n) = c.n.log n + c.log n = O(n.log n)

(Q)What can go wrong if we apply the binary search in an unsorted array?
more precisely,provide an instance where,
binary search algorithm fails to produce desired output.

(Q)We used array data structure to store items, Is there any specific reason for this??

#----code-------------
#need to complete code
if low==hign:
    return points[low]
mid =(low+hign)//2

#wrapper function to call recursive function
def find_rightmost_point(points):
    return find_rightmost_point_recursive(points,0,len(points)-1)

Rightmost Point: (5,0)
T(n)= O(n logab)logn) = O(logn)
    
Time complexity of Linear:O(n)
Time complexity of Binary:O(log n)    

A[11 13 16 19 19 21 29 89 90 99]  x=19
Apply the linear search once the element is found towards left.
mid=(1+10)//2 = 5(index no)

n/2=O(n)
A[11 12 19 19 19 21 29 89 90 99]
LowerBound of x is equal to 3
low=1 high=11   mid= [low+high]/2=6
(at index 6)21 is greater than 19 so low=1 high=6= mid=3
at index 3 19 =19
Time complexity in worst case

#___________________________
#Binary search with some modification
A[1 3 3 5 7 8 8 19] x=8
since take 2 pointers that is low=1 high=9 so 
use binary serch so mid=5
at index 5 element 7 is present ,which is less than 8
i want 8 so it will be right side of 7(at index 5)
so right from index 5 so low=5 high 9 
6+9//2= 7  so at index 7 8 is present
now low=6 high=7 so mid= 7
at index 7, 8 is present

A[1 1 1 1 2 3 4 5] x=1
mid=5  At index 5 2 is present which is grater than 1  so check in left side of indx 5
low=1 high=3



LB(A[1,n],x):
    low=1 ,high=n+1
    while(low<high):
        mid=(low+high)//2
        if(A[mid]< x):
            low = mid+1 #shift low index to 1
         else:
             high= mid

    return low
Ex- [10 20 30 40]
At each iteration of loop size of array is reducing to half.
Recurrence relation is 
T(n)= T(n/2)+c 
which already

Upper bound of x is the position of first element in an array 
that is greater than x

UB(A[1,n], x):
    low=1,high=n+1
    while (low < high):
        mid= (low+high)//2
        if(A[mid] <= x):
            low = mid+1 
        else:
           high = mid
    return high       
            
            
 A[1 2 3 3 3 4]  x=3 lb(3) hb=6 
(Q)            
How to find the number of x's present in an 
Find Lb(x) & Ub(x) & calculate
U(b)-L(b)  

(Q)Suppose instead of selecting the middle element, 
we divide tha array into three parts by selecting the n/3 and 
2n/3 element and proceed with the search in the corresponding segments?
will the complexity remain the same or change?
 
#-------------------------            
A[0 2 2 2 3 4] x=2  found 2 at index 1
if C[mid]==x:
    result=mid
    high=mid-1 
    c[mid]<x: 
        low =mid+1
#------------------------



arr=[0,2,2,2,3,4,5]
x=2
index=find_first_occurrence(arr,x)
if index != -1:
    print(f"First number strictly greater than {x}")
else:
    print(f"No element strictly greater than {x} found") 
    
Ternary:
mid= low +(high-low)/3    0+ (9-0)/3 =3
mid2= high - (high-low)/3  9- (9-0)/3 = 6

logn base3 = logn base2 / log32

(Q)Given a sorted array, find the first and last occurrence of target number in O(log n) time.
(Q)You have an infinte sorted array(You can only access elements via arr[i])
implement binary search to find a target element efficently.   
take 2 pointer : slow,fast
T.C: O(log n) in worst case

Binary search is fastest than Ternary

Have you access on LMS?
Assignment: LinkedList 




















































       
            
            
            
            
            
            
            
            



































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    