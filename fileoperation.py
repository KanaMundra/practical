print("HELLO MOTO")
f1 = open("file1.txt", 'w')
f1.write("THIS IS FILE 1")
f1 = open("file2.txt", 'w')
f1.write("This is FIle 2")

f1 = open("file1.txt", 'r')
data1 = f1.read()

f1 = open("file2.txt", 'r')
data2 = f1.read()

data3 = data1 + data2

f1 = open("file3.txt", 'w')
f1.write(data3)

print(data3)

f1.close()