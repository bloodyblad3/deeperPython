def get_duplicates(lst):
    unique_elements = set()
    duplicates = []

    for element in lst:
        if element in unique_elements:
            duplicates.append(element)
        else:
            unique_elements.add(element)

    return duplicates

my_list = [1, 2, 3, 2, 4, 3, 5, 6, 1, 7, 7, 8, 9, 8]
result = get_duplicates(my_list)
print(result)