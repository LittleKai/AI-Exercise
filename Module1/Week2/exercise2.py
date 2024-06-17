def exercise2(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

string = 'Happiness'
print(exercise2(string))

string = 'smiles'
print(exercise2(string))