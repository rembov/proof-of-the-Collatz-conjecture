n = int(input('Введите натуральное число\n'))


def negr(n):
    k = 0
    while (n != 1):

        if n % 2 == 0:
            n = n // 2
            k += 1
            print(n, k)

        else:
            n = 3 * n + 1
            k += 1
            print(n, k)
    return n, k


print(negr(n))
