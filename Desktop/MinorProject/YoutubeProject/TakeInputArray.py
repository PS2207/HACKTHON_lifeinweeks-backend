n = int(input())
arr = [int(input()) for i in range(n)]  #can create a list using list() function, or using []
arr.append(2)# add one more element in list use append(),this doesn't return value
print(arr)
'''
I/p:
3 #no of elements in array
4
5
6
O/p: [4, 5, 6, 2]
'''
#_______________________________________________________________
n=int(input())
arr=list(map(int, input().split()))
if len(arr) != n:
    print(f"Error: Expected {n} elements but got {len(arr)}.")
else:
    print(arr)
'''
i/p:
3
4 5 6 7 
o/p: Error: Expected 3 elements but got 4. 
''' 
#_____________________________________________
#Adding element in a list
arr=[3,5,7,8,9,2]
arr.extend([0,1,2])
print(arr)  #[3,5,7,8,9,2,  0,1,2]
#-------------------------------
arr=[3,5,7,8,9,2]
arr.insert(2,88)
print(arr) #[3,5,88,7,8,9,2]
#___________________________________________

#Delete elements from a list/array
arr=[3,5,7,8,9,2]
arr.remove(9)
print(arr) #delete specific element, here 9.  i/p:[3,5,7,8,2]
#----------------------------------------------------------
arr=[3,5,7,8,9,2]
arr.pop(2) #delete element by index 2 & return,without index it removes last element.
print(arr) # i/p:[3,5,8,9,2] 
#-------------------------------
arr=[3,5,7,8,9,2]
del arr[3]  #delete by index
print(arr) # i/p:[3,5,7,9,2]
#-------------------------------
arr=[3,5,7,8,9,2]
del arr[1:5] # use 'del [start.stop]' to delete a range, i/p:[3 , 2] 
print(arr)
#-------------------------------
arr=[3,5,7,8,9,2]
arr.clear() #delete all
print(arr) # []
#___________________________________
#________________________________________________________________  
'''
#Take Array Input-
1.Using split() for space-separated input
2.Using split() for comma-separated input
3.Taking input for a fixed-size array
4.Using NumPy for numerical operations

import numpy as np
np.array(list(map(int, input().split())))
'''
n1 = int(input("  Enter a number:   ").strip(" "))
print(n1)
#lst=input().split()  # 2 3 5
#lst= map(str, input().split())
lst= list(map(str, input().split()))
#lst= list(map(int, input().split()))
#lst= "".join(map(str, input().split()))
print(lst)


'''
#arr=list(map(int,input().split()))
arr = ",".join(map(str, input().split()))
print(arr)
'''
'''
_________________________________________
1).arr=list(map(int,input().split()))
4
1 3 5 6
[1, 3, 5, 6]
_________________________________________________
2). [1 3 5 6]    
# for this - use
 arr = " ".join(map(str, input().split()))
 print("["+arr+"]")
________________________________________________
3).arr = " ".join(map(str, input().split()))
4
1 3 5 6
1 3 5 6
________________________________________
4).arr=list(map(int,input().split())) 
print(*arr) # 1 3 5 6

______________________________________________
5).arr = ",".join(map(str, input().split()))
4
1 3 5 6
1,3,5,6
___________________________________________
'''
'''
1).input().split() - reads user input as a single string.
Reads a line of input (always in string format) from a user & converts/splits it into list of sub-string (words) based on white space by default.

2).map(int,...) - converts each string in the list to an integer.  
  or apply int() function to each element(which is always in string format element).
  list(map(int, input().split()))

3).map(str,...) - converts each element string or apply str() function to each element(that is always in string format).
               "".join(map(int, input().split()))
list(...) - collects integers into a list
"".join(map(str, input().split())) - joins  elements/strings of the list into a single string without spaces.
*varName - unpacks the list, so that each element is printed with a space in between.

'''

1.All Problems
  Decidable(Solvable by an algorithm)
  Undecidable(No algorithm exists, e.g. Halting Problem)
2 Decidable Problems:
  Tractable: Solvable in polynomial, e.g. P)
  Example:Sorting, Sorting Path
  Intractable: Require superploynomial/exponential time, e.g, NP-Complete.
  Example: Traveling Salesman, Boolean SAT
P and Np problems:
  P: Problems solvable in polynomial time.
  NP: Problems verifiable in polynomial time.
  Open question: Is P = NP? (Unresolved since 1971)
  Implications: A proof would revolutionize cryptography, optimization, and more.











