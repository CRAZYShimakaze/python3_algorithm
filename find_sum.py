def find_sum(lis, target):
    answer_dict = {}
    answer = []
    for item in lis:
        if (target - item) not in answer_dict:
            answer_dict[item] = target - item
        else:
            answer.append([item, target - item])
            answer_dict.pop(target - item)
    return answer


lis = [1, 3, 34, 25, 6, 8, 4, 2, 2]
print(find_sum(lis, 7))
