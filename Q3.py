def printPascal(n):
    for i in range(n):

        for j in range(n - i):
            print(" ", end="")
        C = 1

        for j in range(i + 1):
            print(C, end=" ")
            C = int(C * (i - j) / (j + 1))
        print(" ")

n = int(input("Enter Rows: "))

printPascal(n)