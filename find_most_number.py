def find_most_number(array):
    number = array[0]
    cnt = 1
    for item in array[1:]:
        if number == item:
            cnt += 1
        elif cnt - 1 == 0:
            number = item
            cnt = 1
        else:
            cnt -= 1
    return number


list = [1, 1, 2, 3, 1, 2, 2, 2]
print(((find_most_number(list))))
