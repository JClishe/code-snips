#dictionaries are changeable, unordered collection of key:value pairs
#they are fast because they use hashing and allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['Russia'])

print(capitals.get('Russia')) #using the get method is safer than printing the key as in the first example. If you print the key and it doesn't exist, the program will error. If you use the get method and it doesn't exist, it will return None

print(capitals.keys()) #print the keys without the values

print(capitals.values()) #print the values without the keys 

print(capitals.items()) #print all keys and values


#use the update method to both add a new key:value pair as well as change an existing one
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})

for key,value in capitals.items():
    print(key, value)