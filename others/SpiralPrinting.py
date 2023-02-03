# spiral printing

def spiral_print(rows, columns, test):
    r = 0  # i is starting row index
    c = 0  # j - starting column index
    # i is the iterator
    while r < rows and c < columns:
        for i in range(c, columns):
            print(test[r][i], end=" ")

        r += 1

        for i in range(r, rows):
            print(test[i][columns - 1], end=" ")

        columns -= 1

        if r < rows:

            for i in range(columns - 1, (c - 1), -1):
                print(test[rows - 1][i], end=" ")

            rows -= 1

        if c < columns:
            for i in range(rows - 1, r - 1, -1):
                print(test[i][c], end=" ")

            c += 1


# function call
test = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

rows = len(test)
columns = len(test[0])
spiral_print(rows, columns, test)
