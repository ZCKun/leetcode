def fib(n):
    tail = [0, 1]
    for i in range(1, n):
        tail.append(sum(tail[-2:]))
    return tail[-1]


if __name__ == '__main__':
    print(fib(4))
