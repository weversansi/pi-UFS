string1 = input()
string2 = input()

for letra in string2:
    string1 = string1.replace(letra, "")

print(string1)