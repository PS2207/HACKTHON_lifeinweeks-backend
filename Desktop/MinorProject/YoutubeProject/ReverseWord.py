'''
#______________________________________________________________
n=int(input())#read no of string line
s=[input() for i in range(n)] #read n strings line, & collect in a list named s.
print(s) # ['hey hi', 'wow nice', 'hello world']
print(s[::-1])  # ['hello world', 'wow nice', 'hey hi']
#______________________________________________________________
'''
'''
n=int(input())
s=[input() for i in range(n)]
words=[]
for _ in range(n):
    for word in s.split():
        words.append(word)
print(words[::-1]) 
'''
'''
s=[input().split() for _ in range(3)] 
print(*s[::-1])  
'''
'''
s=[]
for _ in range(3):
    s += input().split()
print(*s[::-1])    
'''
s= [word for _ in range(3) for word in input().split() ]  
print(*s[::-1])