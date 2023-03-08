#arguments preceded by an identifier when we pass them to a function

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Clishe",first="Jason",middle="Eric") #when we use an identifier (first, middle, last) to pass the arguments into the function, it doesn't matter which order we pass them in. The function will assemble them based on the order of the identifiers
