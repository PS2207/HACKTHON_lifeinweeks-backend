#check max number
#arr=list(map(int, input().split()))
arr=[44,23,5,43,5,46,59] # max=59, but if 5 is encounterd so max=44
max=arr[0]
for num in arr:
    if num>max:
      max=num
    if num==5: # if 5 is encounterd
      break   #44, loop stops if 5 is encountered & print max
print(max) #44
#____________________________________________________________________
#Check If array is sorted  
#--------------------------------------- 
#1.Using sorted() method
#arr= list(map(int, input().split()))
if arr == sorted(arr):
    print("Yes")
else:
    print("No") 

#---------------------------------------------------------    
#2.Using For loop
arr=[44,23,5,43,5,46,59] 
is_sorted =False
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]: # or if arr[i] > arr[i+1] is_sorted=False when var is_sorted=True
        is_sorted = True
        break
if is_sorted:
   print("Yes") 
else:
    print("No")
#---------------------------------------------------------    
#3.Using all()
if all(arr[i] <= arr[i+1] for i in range(len(arr)-1) ) :
    print("Yes")
else:
    print("No")    

#---------------------------------------------------------
#Using 
