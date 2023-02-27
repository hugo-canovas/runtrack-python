nbr = int(input("Entrez votre nombre :"))

with open('data.txt', 'r') as file:
    f = file.read().split()

i=0
for words in f:
    word = len(words)
    if word == nbr:
        i += 1
print(i)