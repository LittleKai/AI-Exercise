def max_window(num_list, k):

    max_wd = []
    i = 0
    while i < len(num_list) - k + 1:
        max_wd.append(max(num_list[i:i + k]))
        i += 1
    return max_window


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

print(max_window((num_list, k)))
