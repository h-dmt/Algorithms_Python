def eight_queen_solutions():
    table = [['-' for _ in range(8)] for _ in range(8)]
    right_diags = [False] * 15
    left_diags = [False] * 15  # index from -7 to 7!!
    columns = [False] * 8

    def can_place_queen(col, row):
        l_idx = col - row if col - row >= 0 else abs(col - row) + 7
        if columns[col] or right_diags[row + col] or left_diags[l_idx]:
            return False

        return True

    def set_queen(row, col):
        l_idx = col - row if col - row >= 0 else abs(col - row) + 7
        table[row][col] = '*'
        columns[col] = True
        right_diags[row + col] = True
        left_diags[l_idx] = True

    def remove_queen(row, col):
        l_idx = col - row if col - row >= 0 else abs(col - row) + 7
        table[row][col] = '-'
        columns[col] = False
        right_diags[row + col] = False
        left_diags[l_idx] = False

    # -- BACKTRACKING --
    def put_queens(row):
        if row == 8:
            print_table(table)
            return

        for col in range(8):
            if can_place_queen(col, row):
                set_queen(row, col)
                put_queens(row + 1)
                remove_queen(row, col)

    put_queens(0)


def print_table(solution):
    [print(*s) for s in solution]
    print()


eight_queen_solutions()
