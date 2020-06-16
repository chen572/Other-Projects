def is_pythagorean_in_list(input_list):
    if len(input_list) < 3:
        return False
    for i in input_list:
        if i < 0:
            input_list.remove(i)
    input_list.sort()
    for a in input_list:
        for b in input_list[1:]:
            for c in input_list[2:]:
                if a ** 2 + b ** 2 == c ** 2:
                    return True
    else:
        print(input_list)
        return False


print(is_pythagorean_in_list([1, 4, 9, 16, 25]))