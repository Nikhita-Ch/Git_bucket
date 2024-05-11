# f= open('file.txt', 'r')
# for a in f:
#     print(a)

import os
path= 'file.txt'
# printing content of file with the help of a function
def reading_file():
    if(os.path.exists(path)):
        file= open('file.txt', 'r')
        for each in file:
            print(each)
    else:
        print("no such file or directory found")

reading_file() #function calling

# directly printion the content of the file
# file= open('simple.txt', 'r')
# print(file.read())

# reading file with the help of with statement
# with open("simple.txt") as file:
#     data= file.read()
# print(data)

# opening the for write mode
file= open('file.txt', 'w')
file.write("the content of the file is overwridden")
# file.close()

reading_file()

#another method to write into the file
# with open('simple.txt', 'w') as data:
#     data.write("this is another method to write in the file")
#     data.close()

# method to append into the file
f= open('file.txt', 'a')
f.write("\nwe can append into it in append mode")
# f.close()
reading_file()

# method to copy the content of one file to another
# with open('simple.txt','r') as firstfile, open('another.txt','a') as secondfile: 
#     for line in firstfile: 
#         secondfile.write(line)
# def abc(f1, f2):
#     for line in f1:
#         f2.write(line)

# if(os.path.exists("f1.txt")):
#     f1= open("f1.txt", "r")
# if(os.path.exists("f2.txt")):
#     f2= open("f2.txt", "a")
# abc(f1, f2)

# a= list({5:"five", 7:"seven"})
# print(a)