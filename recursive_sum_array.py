numbers = [int(n) for n in input().split()]


def calc_sum(n, idx):
    # BASE CASE
    if idx == len(n) - 1:
        return n[idx]
    # RECURSIVE CALL
    return n[idx] + calc_sum(n, idx + 1)


print(calc_sum(numbers, 0))
