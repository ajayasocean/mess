# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, X):
    days_taken = 1
    max_dfclty = -9999999999999999
    min_dfclty = 9999999999999999
    for dfclty in D:
        if dfclty > max_dfclty:
            max_dfclty = dfclty
        if dfclty < min_dfclty:
            min_dfclty = dfclty
        diff = abs(max_dfclty - min_dfclty)
        if diff > X:
            days_taken += 1
            max_dfclty = min_dfclty = dfclty
    return days_taken

if __name__ == '__main__':
    mission_difficulty_list = [1,12,10,4,2]
    difficulty_diff = 4
    days = solution(mission_difficulty_list, difficulty_diff)
    print(f"Number of days to finish mission: {days}")


# write unit test on above code
