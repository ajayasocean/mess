
def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if string_list[left] in vowels and string_list[right] in vowels:
            string_list[left], string_list[right] = string_list[right], string_list[left]
            left += 1
            right -= 1
        elif string_list[left] in vowels:
            right -= 1
        else:
            left += 1

    return ''.join(string_list)


def main():
    str = 'hello'
    print(reverse_vowels(str))


if __name__ == '__main__':
    main()
