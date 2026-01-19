#.upper() for upperCase
#.lower() for lowerCase
name = "John Doe"
print(name.upper())  # prints JOHN DOE
print(name.lower())  # prints john doe

#.strip() removes space from the beginning and the end of the string
greeting = "   Hello, World!   "
print(greeting.strip())  # prints "Hello, World!"

#.replace(old, new) replaces old substring with new substring
text = "I like apples"
print(text.replace("apples", "oranges"))  # prints "I like oranges"

#.split(separator) splits the string into a list based on the separator
sentence = "Hello, how are you?"
words = sentence.split(" ")
print(words)  # prints ['Hello,', 'how', 'are', 'you?']