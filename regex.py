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

""" print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

# |-is used to match either the expression before or the expression after it. It is also known as the alternation operator.
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats.")) """

# *- is used to match zero or more occurrences of the preceding character.
# .*- is used to match zero or more occurrences of any character except a new line.
""" print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn")) """


""" print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil")) """

# ?- is used to match zero or one occurrence of the preceding character.
""" print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
 """

#\- is used to escape special characters, so they can be used in a search string without invoking their special meaning.
""" print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com")) """


# /w- is used to match any alphanumeric character (letters and digits) and the underscore character.
""" print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another")) """

""" print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia")) """


""" pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1")) """

# *- is used to match zero or more occurrences of the preceding character.
# \w- is used to match any alphanumeric character (letters and digits) and the underscore character.
# \d- is used to match any digit character (0-9).
# {}- is used to specify the number of occurrences of the preceding character or group.
# \b- is used to match a word boundary, which is the position between a word character and a non-word character.
# !- is used to match the exclamation mark character literally.