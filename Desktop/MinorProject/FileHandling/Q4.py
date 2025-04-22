
i=0 #initial value
while i<3: #0,1,2
  #1st iteration: 0<3 ->True, so increment 0 by 1 so i=1 | 
  #2nd iteration: 1<3 ->True, so increment 1 by 1 so i=2 | 
  #3rd iteration: 2<3 ->True ,so increment 2 by 1 so i=3 | 
  #now Check 3<3 -> False . loop stops so i=3 print 3
    i+=1
print(i)#3

my_list=[1,2,3]
result=my_list.append(4)#append doesn't create a new list or return updated list
print(result)#it always returns None
print(my_list)#[1, 2, 3, 4]


#Python doesn't allow non-default parameter to follow default parameter except parameter
#Invalid case
'''
def add(a=5,b): #a default parameter, b non-default parameter
    return a+b
print(add(10))#default parameter
'''
#Valid case
def add(a,b=5):#a is non-default parameter, b is default parameter
    return a+b
print(add(10))#15 (10 is assigned to a & b takes it default value of 5)

#*args (positional arguments)
#*kwargs  (keyword arguments)
def positional_arg(a,*kwargs):
    print(a,*kwargs)#10 20 30
positional_arg(10, 20,30)   

n = int(input()) # takes an integer input n from user
s='abcdefghijklmnopqrstuvwxyz' # Define string contains all lowercase english letters
d={} # initialize dictionary: empty dictionary d is created
for i in range(26):
    a= s[i]
    #print(s[i])
    #print(a)#a,b,c...z(vertical)
    #print(i)#0,1,2...25
    #print(s) #abcd...z (26times)
    d[a]= n+i
    #print(d[a])#start from input upto total 26
# 2nd loop iterates over the dictionary, printing each letter & its assigned value in the format :key-value    
for j in d:    
    print(j ,"-" , str(d[j]))#Python doesn't allow direct concatenation of strings & integers so str(d[j])

























 