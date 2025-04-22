a,b,c= map(int,input().split()) # Input should be integer value
#a,b,c= input().split() # input will be treated as string

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





