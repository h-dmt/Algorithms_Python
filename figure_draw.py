
def draw_figure(n):
    if n == 0:
        return

    print('*' * n)  # <----- Pre recursive behaviour
    draw_figure(n - 1)
    print('#' * n)   # <---- Post recursive behaviour


draw_figure(int(input()))
