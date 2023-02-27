#sort () method = used with lists
#sort () function = used with iterables

#sort method
students = ["Squidward","Sandy","Patrick","Spongebob","Mr. Krab"]

students.sort()

for i in students:
    print(i)

#===

#sort function
students = ("Squidward","Sandy","Patrick","Spongebob","Mr. Krab")

sorted_students = sorted(students)

for i in sorted_students:
    print(i)

#sorting a list of tuples using an index position besides the first
students_2 = [("Squidward", "F", 60),
              ("Sandy", "A", 33),
              ("Patrick", "D", 36),
              ("Spongebob", "B", 20),
              ("Mr. Krab", "C", 78)]

grade = lambda grades:grades[1]
students_2.sort(key=grade)

for i in students_2:
    print(i)


