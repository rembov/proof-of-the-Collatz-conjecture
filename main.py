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

if __name__ == "__main__":
    n = int(0)
    while (n < 1):
        n = int(input("Введите натуральное число: "))
    res, steps = negr(n)
    print(f"Результат: {res}\nКоличество шагов: {steps}")
