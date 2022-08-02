def reverse(string):
    assert isinstance(string, str), "Input should be a string"
    assert len(string) >= 2, "Input should have length more or equal to 2"
    string_list = list(string)
    reversed_string = []
    string_list_length = len(string_list) - 1
    # for i in range(string_list_length):
    #     last_letter = string_list[string_list_length-1-i]
    #     reversed_string.append(last_letter)

    for i in range(string_list_length, -1, -1):
        last_letter = string_list[i]
        reversed_string.append(last_letter)

    return "".join(reversed_string)

def reverse2(string):
    assert isinstance(string, str), "Input should be a string"
    assert len(string) >= 2, "Input should have length more or equal to 2"
    string_list = list(string)
    reversed_string = []
    string_list_length = len(string_list)
    for i in range(string_list_length):
        last_letter = string_list[string_list_length-1-i]
        reversed_string.append(last_letter)

    return "".join(reversed_string)

def reverse3(string):
    assert isinstance(string, str), "Input should be a string"
    assert len(string) >= 2, "Input should have length more or equal to 2"
    string_length = len(string)
    reversed_string = []
    for i in range(string_length):
        last_letter = string[string_length-1-i]
        reversed_string.append(last_letter)

    return "".join(reversed_string)


def reverse4(string):
    return "".join(list(string)[::-1])


def reverse5(string):
    return list(string).reverse()


string = "Hi My Name Is Jakub"
reversed_string = reverse(string)
print(reversed_string)
reversed_string = reverse2(string)
print(reversed_string)
reversed_string = reverse3(string)
print(reversed_string)
reversed_string = reverse4(string)
print(reversed_string)
special_string = string
reverse5(special_string)
print(special_string)
