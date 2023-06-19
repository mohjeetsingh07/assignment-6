n = int(input("Enter a number: "))

def perfect(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")

perfect(n)