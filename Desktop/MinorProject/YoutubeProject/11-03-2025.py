#Fibonacci sequuence:
#A sequence of numbers in which an element in the sequence is the sum of previous elements.
First element is 0 and 2nd elements is 1
0 1 1 2 3 5 8 13 21 24
Recursion Relation:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
T(n)= T(n-1) + T(n-2)

Level of tree:
                      T(n)               2pow0
             T(n-1)                T(n-2)    2pow1
      T(n-2)        T(n-3)      T(n-3)  T(n-4) 2pow2
2T(n-3)  T(n-4)   T(n-4) T(n-5)          2pow3
3T(n-3)T(n-4)
.
.
T(1)          2k

No of funtion to be called for this fibonacci series use recursion function
T(n)  a T(a/b) + f(n)  function in this form so master method can't be applied
Fibonacci sequence:
Time complexity = O(2^n)
Pretty Bad
Can be improved with dynamic programing and other methods.
a=2 r=2
2 rasise 1+ 2 raise 2 + 2 raise 3+......+ 2 raise 2
s = a r raise n -1 / a2-1   = 2 x(2 pow n - 1 /) /2-1  = O(2 to the pow n)

Placing a tile:
(Q)Given a 2*n grid and 1*1 tile, i want to find out number of ways to completely fill the grid.
The tiles can be placed from left to right.
Write the recursive function and solve the problem.

Climb Stairs:
A person is standing at the bottom of a staircase with n steps
They can take 1step, 2step, 3steps at a time.
Find number of ways they can reach the stair case. n=4
1 1 1 1-     2 1 1 *
1 2 3 -      3 1 *
1 3 -
2 2 -
T(n) =T(n-1) + T(n-2) 
30 + 31 + 32 + 33+......+3n   a=3  r=3  s=(arraisen-1)/r-1
O(3^n)


def fibonacci_recursive(n):
    if n<=1:
        return n
    if n==1:
        return 1
    return count_ways(n-1) + count_ways(n-2)+count_ways(n-3)
print(count_ways(4))
print(count_ways())

9258436278






























