def levenshtein_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    if n == 0:
        return m
    if m == 0:
        return n

    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                insertion = d[i - 1][j] + 1
                deletion = d[i][j - 1] + 1
                substitution = d[i - 1][j - 1] + 1
                d[i][j] = min(insertion, deletion, substitution)

    return d[n][m]

str1 = "kitten"
str2 = "sitting"

distance = levenshtein_distance(str1, str2)
print("Levenshtein distance between", str1, "and", str2, "is:", distance)

str1 = "yu"
str2 = "you"

distance = levenshtein_distance(str1, str2)
print("Levenshtein distance between", str1, "and", str2, "is:", distance)