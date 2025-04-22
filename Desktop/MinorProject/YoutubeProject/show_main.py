#both ways we can use
#way-1
'''from show import display
display()'''

#way-2
import show 
show.display()

#but if we run this show_main.py file that contains only 'import show ',
#it won't print anything from show.py unless you call show.disply() explicitly,
# bcz i have called functoin inside this if __name__ == "__main__" block. 

for i in range( 4):
    print(i)
    

