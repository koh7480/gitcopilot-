def factorial(n):
    if n < 0:
        raise ValueError("음수는 factorial을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    for i in range(11):
        print(f"{i}! = {factorial(i)}")
