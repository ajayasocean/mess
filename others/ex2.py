# returning list of items from a given list that are sum of any two items from that list.
lst = [2, 3, 1, 1, 5, 4, 6, 9, 10]
result = []


def get_item_sum(lst):
    for each in lst:
        for num1 in lst:
            for j in range(len(lst)-1):
                if each != num1 + lst[j]:
                    continue
                else:
                    if each in result:
                        continue
                    else:
                        result.append(each)

    return result


if __name__ == '__main__':
    print(get_item_sum(lst))




