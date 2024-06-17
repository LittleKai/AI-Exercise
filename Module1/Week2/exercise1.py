def exercise1(num_list, k):

    max_window = []
    i = 0
    while i < len(num_list) - k + 1:
        max_window.append(max(num_list[i:i + k]))
        i += 1
    return max_window

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

max_window = exercise1(num_list, k)
print(max_window)