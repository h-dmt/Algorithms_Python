def gen_01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        gen_01(idx + 1, vector)


n = int(input())
v = [0] * n


gen_01(0, v)
