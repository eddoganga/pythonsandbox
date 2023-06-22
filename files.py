# has a function for ceating, reading, updating and deleting files

#open a file
myFile = open('myfile.txt', 'w')

#get some info

print('name:', myFile.name)

#write to the file
myFile.write('i love it here i hate it it here')

#append to file
myFile = open('myfile.txt', 'a')
myFile.write('heell yeah lets ride')


#read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)