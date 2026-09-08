from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    # third_last = my_list[-3]
    # second_last = my_list[-2]
    # last = my_list[-1]

    # return [third_last, second_last, last]
    third_last_position = len(my_list) - 3
    return my_list[third_last_position:]


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
