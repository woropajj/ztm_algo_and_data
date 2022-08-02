

def return_first_recurring_character(array):
    inside_array = [array[0]]
    for i in array[1:]:
        if i in inside_array:
            return i
        inside_array.append(i)
    return None


print(return_first_recurring_character([2, 5, 5, 2, 3, 5, 1, 2, 4]))
print(return_first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(return_first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(return_first_recurring_character([2, 3, 4, 5]))


def return_first_recurring_character2(array):
    hashlol = {}
    for i in array:
        if str(i) in hashlol:
            return i
        else:
            hashlol[str(i)] = i
    return None


print(return_first_recurring_character2([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(return_first_recurring_character2([2, 5, 5, 2, 3, 5, 1, 2, 4]))