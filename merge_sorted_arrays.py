from builtins import isinstance


def msa1(ar1, ar2):
    total = ar1 + ar2
    return sorted(total)


def msa2(ar1, ar2):
    assert isinstance(ar1, list), "Input 1 should be a list"
    assert isinstance(ar2, list), "Input 2 should be a list"

    # check input
    if len(ar1) == 0:
        return ar2
    elif len(ar2) == 0:
        return ar1

    merged_array = []
    i = 0
    j = 0

    while i < len(ar1) and j < len(ar2):
        if ar1[i] <= ar2[j]:
            merged_array.append(ar1[i])
            i += 1
        elif ar2[j] < ar1[i]:
            merged_array.append(ar2[j])
            j += 1

    return merged_array + ar1[i:] + ar2[j:]


def msa3(array1, array2):
    merged_array = []
    array1_item = array1[0]
    array2_item = array2[0]
    i = 1
    j = 1
    while array1_item or array2_item:
        if array1_item < array2_item:
            merged_array.append(array1_item)
            array1_item = array1[i]
            i += 1
        else:
            merged_array.append(array2_item)
            if j < len(array2):
                array2_item = array2[j]
            else:
                merged_array.append(array1_item)
                break
            j += 1

    return merged_array


array1 = [0, 3, 4, 31]
array2 = [4, 6, 30, 31, 32]

result = msa1(array1, array2)
print(result)
result = msa2(array1, array2)
print(result)
result = msa3(array1, array2)
print(result)
