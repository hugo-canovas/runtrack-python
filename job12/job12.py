import string
import re

with open('data.txt', "r") as file:
    f = file.read()
    #f = file.read().split()
    result = len(re.findall(r'\w+', f))
    #result = sum([i.strip(string.punctuation).isalpha() for i in f])
    print(result)
