"""WAP to find occurrence word in given string "Creating aws and aws maintaining BDD behave tests using python, behave, pandas, aws, sql , boto and pytest"
( O/P: Creating: 1, aws: 2... and so on)"""""

def main():

    _str = "Creating aws and aws maintaining BDD behave tests using python, behave, pandas, aws, sql , boto and pytest"
    word_list = (_str.split(" "))
    # print(word_list)
    word_list.sort()
    new_list = []
    for each in word_list:
        each = each.replace(",", "").lower()
        new_list.append(each)
    new_list.remove("")
    new_list.sort()
    print(new_list)
    set_word_list = set(new_list)
    lst_set_word_list = list(set_word_list)
    lst_set_word_list.sort()
    print(lst_set_word_list)


    def get_occurence(lst, ele):
        count = 0
        for each in lst:
            if each == ele:
                count += 1
        return count

    dup = {}
    for each in new_list:
        count = get_occurence(new_list, each)
        dup[each] = count
    print(dup)



if __name__ == '__main__':
    main()