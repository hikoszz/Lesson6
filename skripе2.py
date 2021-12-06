from os import close


#f = open('C://Users/1/Desktop/Lesson 3/input.txt')
#data = f.read()
#print(data.split())
#f.close()
input_file = open("C://Users/1/Desktop/Lesson 3/input.txt", "r")
output_file = open("C://Users/1/Desktop/Lesson 3/output.txt", "w")
line = input_file.readline().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])
 
a1 = a // 2
b1 = b // 6
c1 = c // 1
 
ans = min(a1, b1, c1)
 
print(ans)
output_file.write(str(ans) + "\n")