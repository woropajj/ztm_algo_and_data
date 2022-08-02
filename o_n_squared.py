boxes = ['a', 'b', 'c', 'd', 'e']


def log_all_pairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])


def log_all_pairs2(array):
    for i, item in enumerate(array):
        for j, item2 in enumerate(array):
            print(array[i], array[j])


log_all_pairs(boxes)
print("przerwa")
log_all_pairs2(boxes)
