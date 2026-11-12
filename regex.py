""" log= "July 31 07:51:48 mycomouter bad_process[12345]:ERROR Performing package upgrade"
regex = r"\[(\d+)]"
index = log.index("[")
print(log[index+1:index+6]) """

import re


""" log= "July 31 07:51:48 mycomouter bad_process[12345]:ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1]) """

# .-represents any character except a new line
# ^-represents the beginning of a string
# $- represents the end of a string

# result = re.search(r"aza", "plaza")
# print(result)

""" result = re.search(r"aza", "bazaar")
print(result) """

""" result = re.search(r"aza", "maze")
print(result) """

# print(re.search(r"^x", "xenon")) 

# print(re.search(r"p.ng", "penguin"))

""" print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge")) """

# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# print(re.search(r"[Pp]ython", "Python"))

""" print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9")) """

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))



