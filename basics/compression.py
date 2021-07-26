def print_rle(s):
    i = 0
    _return_this = ''
    while i < len(s) - 1:

        # Counting occurrences of s[i]
        count = 1

        while s[i] == s[i + 1]:

            i += 1
            count += 1

            if i + 1 == len(s):
                break

        _return_this += str(s[i]) + (f'{str(count)}' if count > 1 else '')
        i += 1

    return _return_this


# Driver Code
if __name__ == "__main__":
    # function calling
    _o = print_rle("abaasass")
    print(_o)
