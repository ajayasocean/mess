def solution(S):
    sb = list(S)
    length = len(S)

    for i in range(1, length-1):
        if sb[i] == '-' and sb[i-1] == 'H' and sb[i+1] == 'H':
            sb[i] = 'water'
            sb[i-1] = 'Da'
            sb[i+1] = 'Da'

    for i in range(0, length):
        if sb[i] == 'H':
            if i-1 >= 0 and sb[i-1] != 'water' and sb[i-1] == '-':
                sb[i-1] = 'water'
                sb[i] = 'Da'
            elif i+1 <= length-1 and sb[i+1] != 'water' and sb[i+1] == '-':
                sb[i+1] = 'water'
                sb[i] = 'Da'
            else:
                return -1

    count = 0
    for i in range(0, length):
        if sb[i] == 'water':
            count += 1
        if sb[i] == 'H':
            return -1

    return count


if __name__ == '__main__':
    res = solution("-H-H-H-H-H-H")
    print(f"Result: \n{res}")

