#parameter that will pack arguments into a dictionary. Similar to args except it packs arguments into a dictionary instead of a tuple

def hello(**kwargs): #2 astericks denotes kwargs
    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="Jason",middle="Eric",last="Clishe")

print("===")

#another way of writing above code by using a for loop to iterate through the arguments
def hello(**kwargs):
    print("Hello")
    for key,value in kwargs.items():
        print(value)

hello(first="Jason",middle="Eric",last="Clishe")