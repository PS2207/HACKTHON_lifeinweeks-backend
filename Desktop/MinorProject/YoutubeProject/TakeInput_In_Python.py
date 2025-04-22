'''
(Q)How to take multiple integer inputs from user in Python & print it ?
Ans: a,b,c, .. = map(int, input().split())
This line is a concise way to take multiple space-separated integer inputs from the user,
& assigned them to the variables a,b,c.

Let's understand, How it works step-by-step:-
    
# input(): This method reads a line of input from the user as a single string. 
  Ex- input: 4 5 6 | output: 4 5 6 (as string)
# split(): This method splits/breaks the input string into a list of substring.
  Ex- input: 4 5 6 | output:['4', '5', '6']
# map(int,..): This function applies the int function to each element in the list returned by split().
  Ex- input: 4 5 6 | output: 4 5 6 (as integers)
'''
print("----Example-1----")
a=input() # Hello world
print(a)  # Hello World

print("----Example-2----")
b=input().split() # Hi How are you
print(b)          #['Hi', 'How', 'Are', 'You']

print("----Example-3----")
a,b,c= map(int, input().split()) # 4 5 6

print('a =',a, 'b =',b, 'c =',c)  # a = 4 b = 5 c = 6 ( Using commas)
print('a = ' +str(a)+ ' b = '+str(b)+ ' c = '+str(c)) # string concatenation using +.
print(f"a = {a} b = {b} c = {c}")
#--------
#Note: The best approach is f-string,coz it is clear,readable,flexible.




