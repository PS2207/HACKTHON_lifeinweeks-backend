#Naive Recursive approach to find fibonacci. 
#T.C= O(2^n), if n=1 ,T.C=2 |  If n=2 ,T.C=2^2=4 | If n=3 ,T.C= 2^3=8
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
n=3
print(fib(n))
#__________Bottom-up (Tabulation)_________________
def fib(n):
    if n<=1:
        return n
    #Base cases of Fibonacci sequence : fib(0)=0, fib(1)=1 initailly set this manually
    #creating a list dp of size n+1 for storing fibonacci numbers from 0 to n
    #initially it's filled with all 0s
    dp = [0] * (n+1) # fill 0 in all index 0,1,2,3,4
    dp[1] = 1   #manually set so that fib(1)=1 at index 1 ,since at index 0 fib(0)=0 alrready set above
    
    for i in range(2, n+1):  #we fill in the list from index 2 to n using loop, bcz at 0  =0 at 1=1
        dp[i] = dp[i-1] + dp[i-2]  #line implements fibonacci recurrence. add previous 2 values to get next value in fibonacci series.
    return dp[n]     #return nth fibonacci no.. from the dp list, here 2
n=4
print(fib(n))#3

n= int(input())
arr=list(map(int, input().split()))
sorted_arr= sorted(arr)
sum=0
for i in range(n):
    sum= sum+i*sorted_arr[i]
print(sum)