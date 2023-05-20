
import string

def largest_factor_lt_k(n, k):
    for i in range(k-1, 0, -1):
        if n % i == 0:
            return i
    return None

def solution(N):
    alphabet = string.ascii_lowercase
    if N <= 26:
        return alphabet[:N]
    else:
        lfltk = largest_factor_lt_k(N, 27)
        n_times = N // lfltk # will always be integer
        _str = []
        for a in alphabet[:lfltk]:
            for _ in range(n_times):
                _str.append(a)
        return ''.join(_str)

if __name__ == '__main__':
    n = 15 # number to be tested
    print(f"Result: \n{solution(n)}")



