def char_count(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

string = 'Happiness'
print(char_count(string))

string = 'smiles'
print(char_count(string))
