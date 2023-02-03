"""
are_2_strings_almost_equivalent
"""
from string import ascii_lowercase


def get_char_frequencies(st):

    freq = {char: 0 for char in ascii_lowercase}
    for char in st:
        freq[char] += 1
    return freq


def are_2_strings_almost_equivalent(st, tt):
    result = []
    for idx_s in st:
        for idx_t in tt:
            if len(idx_s) != len(idx_t):
                equivalent = 'No'
                # result.append(equivalent)

            freq_s = get_char_frequencies(idx_s)
            freq_t = get_char_frequencies(idx_t)

            for char in ascii_lowercase:
                if abs(freq_s[char] - freq_t[char]) > 3:
                    equivalent = 'NO'
                    # result.append(equivalent)

            # if no significant difference was found
            equivalent = 'Yes'
        result.append(equivalent)
    return result


if __name__ == '__main__':
    s = ['a', 'b']
    t = ['c', 'd']
    print(are_2_strings_almost_equivalent(s, t))


