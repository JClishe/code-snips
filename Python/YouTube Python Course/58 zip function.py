#aggregate elements from two or more iterables. Creates a zip object with paired elements stored in tuples for each element

#zip(*iterables)

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)

print(type(users))

for i in users:
    print(i)

    