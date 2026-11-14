""" data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
 """

# shell
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))