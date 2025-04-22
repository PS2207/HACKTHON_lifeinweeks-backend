def display():
    print("hello from show") 
#display()   
#it'll print when calling this function, 
#but if we import this file in another file by writing 'import show' it calls display() automatically.
#so we need to write this -
if __name__ == "__main__":
    display()
#now function is inside  if name__ == "__main__"  block   
'''
Why it's good?
bcz it helps organize code better
Avoid unwanted execution of code when importing modules.
Useful for writing testable and reusable modules.
'''










































