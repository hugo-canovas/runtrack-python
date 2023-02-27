text = str(input("Entrez votre texte :"))

files = open("output.txt", "w")
files.write(text)
files.close()

path = open("output.txt", "r")
print(path.read())