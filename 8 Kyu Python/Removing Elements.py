def remove_every_other(my_list):
    # Your code here!
    sorted = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            sorted.append(my_list[i])
    return sorted
