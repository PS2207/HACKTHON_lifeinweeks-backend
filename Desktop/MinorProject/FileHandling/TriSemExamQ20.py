'''
Description:
Given an array of size n, which is strictly increasing and then strictly decreasing in order.
Find out the index (0-based) which is the peak of the array.
Note that the extremities are not considered as peak and there exists a peak which is not at index 0 or n-1
Input Description:
    
Output Description:
   For each test case, print the answer: The peak index.

Input:
2
3
10 20 11
5
1 3 6 5 4
Output:
1
2
'''   
''' 
def array(arr):
    
def main():
    test_cases=int(input())
    for i in range(test_cases):
        n=int(input())
        arr= list(map(int, input().split())) 
        result= array(arr)
        print(result)
if __name__= "main()"  :
    main()
'''
#* // + -
#x= 10+5//3-3*4/2
x=10/6*2-5+1
print(x)   
     
#___________________________________________________________________________________________________________________
'''
(Q)How to take multiple integer inputs from user in Python & print it ,then convert it into a list or tuple or set or dictionary?
Ans: a,b,c, .. = map(int, input().split()),To convert- use [] for list, () for tuple, {} for set, {key:value} for dictionary

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
#-------
a=input()
b=input().split()
print(a)
print(b) 
#-------
a,b,c= map(int, input().split())

print('a =',a, 'b =',b, 'c =',c)  #Using commas
print('a =' +str(a)+ 'b ='+str(b)+ 'c ='+str(c)) #string concatenation using +.
print(f" 'a ='{a} 'b =' {b} 'c ='{c}  ")
#--------
#Note: The best approach is f-string,coz it is clear,readable,flexible.
#_______________________________________________

#convert input into list,tuple,set,dictionary
print("\n---Convert input into  List-------")
lst1= list((a,b,c))
lst2= list({a,b,c})
lst3= list([a,b,c])
lst4= [a,b,c]
print(type(lst1))
print(type(lst2))
print(type(lst3))
print(type(lst4))
print(lst1)
print(lst2)
print(lst3)
#______________________________________

print("\n---Convert into tuple-------")
tpl1= tuple((a,b,c))
tpl2= tuple({a,b,c})
tpl3= tuple([a,b,c])
print(tpl1)
print(type(tpl2))
print(type(tpl3))
#____________________________________

print("\n---Convert into set-------")
set1= set((a,b,c))
set2= set({a,b,c})
set3= set([a,b,c])
print(set1)
print(type(set2))
print(type(set3))

#____________________________________

print("\n---Convert into dict-------")
dict1= {a:1,b:2,c:3}
dict2= dict({a:1,b:2,c:3})
print(type(dict1))
print(dict2)
#_____________________________________

#######################################################
































