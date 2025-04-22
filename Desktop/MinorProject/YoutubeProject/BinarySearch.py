'''
Binary Search is a sorting algorithm used to find an element in a sorted array. it follows Divide-And-Conquer paradigm.
steps of binary serach:
1.Find the middle element of the sorted list.  
2.If the middle element matches target, return its index.
3.If the target is smaller than the middle element, search the left half.
4.If the target is larger than the middle element, search the right half.
5.Repeat steps 1-4 until the element is found or the search range is exhausted

Time Complexity: 
Best case:  O(1) (if middle element is the target)
Worst case & Average Case: O(log n)  (Since the list is halved in each step)

Example: For a sorted array [2, 4 ,7 ,10, 15, 20] searching for 10
''' 
def binarySearch(arr,x):
    start,end=  0, len(arr)-1
    is_ascending= arr[start] < arr[end]
    while start <= end: #loop continues as long as start index <=end index, if start exceeds end, that means element is not in array.
        
         mid= (start+end)//2 #find mid index
         if arr[mid] == x:
             return mid #index
         if is_ascending:  #In Binary Search, array should be sorted so if sorted
             if arr[mid] < x: # check right sub-array
                 start = mid + 1
             else:
                 end = mid - 1 #check left
                 
         else:  #if not sorted
             end = mid -1
    return None #or -1     
    
arr=[1,2,3,4,5,6]
x=4
index = binarySearch(arr,x)
if index is not None:
    print(f"{x} is found at index: {index}")
else:
    print("Element is not found")    

#use mid= start + (end - start) in place of mid= start+ end // 2  
#This prevents integer overflow in some languages like c++,(not a problem in Python, but it's a good practice')
#-------------------------------------------------------------------------------------------------------------------------

'''
Place N Queens in N X N chessboard, where No 2 Queens attack each other
No 2 Queens in the same row
No 2 Queens in same column
No 2 Queens in same diagonal

Below is the 4X4 board indicating the placement of queens such that none attacks one another.
[R] []  []  []
[]  []  [] [R]
[]  [R] []  []
[]  []  []  []
it not work


[]  [R]  []  []
[]   []  []  [R]
[R]  []  []   []
[]   []  [R]  []
ALl Queen have been places noone attack each other

CReate a 2D array board[1..N][1..N]
for i <- 1 to N:
     for j <- to N:
         board[i][j] <- 0
return board   
i,j)th position is vaccant No space is there

Pseudocode: is_safe code Function(checks whether Queen is safe at this position or not)      
#Check Column
for i = 1 to row -1 do
  if board[i][col] == 1 then
     return False
 
#Check upper-left diagonal
i = row-1
j = col-1
while i >= 1 and j>=1 do
 if board[i][j] == 1 then
  return False
 i = i-1
 j = j-1

#Check upper-right diagonal
i = row-1
j = col+1 
while i >= 1 and j <= N do
  if board[i][j] == 1 then
     return False
  i = i-1
  j = j+1
return True
End Function  

Function solve/(row, N, board):
    if row>N :
        print_board(board, N)
        return True
    for col= 1 to N do
    if is_safe(row, col , N, board) then
       board[row][col] =1 //place queen
       if solve(row+1, N, board) then
         return True
       else:
         board[row][col]=0 //Backtrack
     end for    
end function    
//call the function solve(1, N,board) 

Complexity Analysis 
#Worst case Time Complexity
we will check all possible choices
N choices for each queen
We check all possibilities
T(N) =O(N^N)   

#Average Time Complexity
There is no strict formula for average case,
because the number of valid configurations varies 

Space complexity is O(n^2)

given an undirected, simple grapg G=(V,E) & an integer m
Assign one of the m colors to each vertex of the graph
Assign colors to vertices one by one.
For each vertex, try all colors from 1 to m.
Before assigning, check if assigning

(Q)How we will represent a graph














    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
















 


















'''




























































