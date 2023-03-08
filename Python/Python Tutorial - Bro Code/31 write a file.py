text = "Hello World\n"

with open('31_test.txt', 'w') as file: #w = write mode
    file.write(text)

text = "Hello World 2\n"

with open('31_test.txt', 'a') as file: #a = append mode
    file.write(text)