with open('domains.xml', "r") as file:
    print(file.read().count('name="domain"'))