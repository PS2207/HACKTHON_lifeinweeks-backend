'''
Divide and Conquer is more than a military strategy;
it is also a method of algorithm design that has created

Algorithm: Divide:If S has at least two elements remove all the elemnts from S and put them into two sequences,
Merge Sort Tree:
 
Divide problem into sub-problem
n= n/2 + n/2
n/2= n/4 + n/4
n/4= n/8 + n/8
n/8= n/16 + n/16 
compute geometric series to find (n log n)
   
85 24 63 45 | 17 31 96 50
divide array into 2 parts let's say s1 s2
s1= 85 24 63 45   s2= 17 31 96 50
again divide into 2 parts:
s3= 85 24 s4= 63 45 
24 45 63 85 
s5= 17 31 s6= 96 50  
17 31 50 96

24 45 63 85
17 31 50 96
24&31

compare 17&24 31&45 50&63 85&96
17 24 31 45 50 63 85 96

Time copmlexity of merge sort:
    Recursion relation using (i)Master method or (ii)Recursion tree
    n = (n/2) +  (n/2) = 2T(n/2) +O(n) Time taken by merginf)
    T(n)= O(n log n)
    
Best case- if array is already sorted don't have to sort just need to check'
Worst case
Average case 
Merge sort always take O(n log n) time complexity in all cases   
Space complexity = O(n)
Stable- Merge Sort, Bubble Sort
Non-stable- selection sort

In-place algorithm doesn't require extra space
'''














