#Factorial of numbers from 1-10 using threads
#Find differnce between both code which is better?
def calculate_factorial(n):
    #n=int(input())
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact   
result= calculate_factorial(5)    
print(result)
#Flexibility:Store return value in a variable .
#the return value can be used in further calculation
#-------------------------------
def calculate_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)    
calculate_factorial(5) #function call 
#Suitable for simple program needing only displays of output
#-----------------------------

from threading import Thread
def calculate_factorial(n):
    fact=1
    for i in range(1,n+1):
     fact*=i
    print(fact) 
t= Thread(target= calculate_factorial, args=(4,)) 
t.start()
#t.join() 
#---------------------------------------------
from threading import Thread 
import time
def calculate_factorial(n):  
    fact=1
    for i in range(1,n+1): 
        fact*=i
        time.sleep(10)#sleep for 10 second 
    print(fact) 
threads=[]
for num in range(1, 5):  
 t= Thread(target= calculate_factorial, args=(num,))
 threads.append(t)
 t.start()


