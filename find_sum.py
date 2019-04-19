def find_sum(lis, target):
    answer_list = []
    answer = []
    for item in lis:
        if item in answer_list:
            answer.append([target - item, item])
            answer_list.remove(item)
        else:
            answer_list.append(target - item)
    return answer


lis = [1, 3, 4, 3, 5, 5, 6, 6, 4, 2, 4, 2, 5]
print(find_sum(lis, 7))
