
lst = [1, 3, 4, 'a', 'b', 'tg', 'a', 1, 3, 2]


def get_dup():
    dup = {}
    for item in lst:
        try:
            dup[item] += 1
        except:
            dup[item] = 1
    return dup
# driver code


if __name__ == "__main__":
    print(get_dup())



