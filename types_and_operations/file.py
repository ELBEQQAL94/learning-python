# make new file
f = open('data.txt', 'w')

# write something in the file
f.write('Hello, World!')
f.write('Something else')

# close file
f.close()

r = open('data.txt')

text = r.read()

print(text.split())