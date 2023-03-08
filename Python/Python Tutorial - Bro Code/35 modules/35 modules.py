#a module is a file containing python code. May contain functions, classes, etc.
#used with modular programming, which is to seperate a program into parts

#import messages 
"""
import messages as msg #we can optionally give the module an alias when we import it

msg.hello() #name of the module we're importing followed by the function we're calling
msg.bye()
"""

#we can optionally import the specific functions we want to use instead of the entire module. When doing so, we can access the function direcly by its name instead of using the module.function notation above
from messages import hello,bye

hello()
bye()

#not recommended but can import all functions in a module with:
#from messages import *






