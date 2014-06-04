import sys
import os


file = open('HelloWorld.txt', "w")
file.write("Hello world in the new file\n")
file.write("and another line\n")
file.write("like in the new world\n")
file.write("I love Andrea")
file.close()

f = open('HelloWorld.txt', 'r+')

print f.readline()
print f.read()



	