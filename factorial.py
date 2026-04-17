def factorial(n):
    if n < 0:
        raise ValueError("음수는 factorial을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print('factorial')
    for i in range(11):
        print(f"{i}! = {factorial(i)}")

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

if __name__ == "__main__":
    print('factorial_recursive')
    for i in range(11):
        print(f"{i}! = {factorial_recursive(i)}")   

