
def sum1(n):
    # complexetiy is O(n)?
    total = 0
    for i in range(n):
        total += 1
    return total

def sum2(n):
    # complexity is O(n^3) I think
    total = 0
    for i in range(n):
        for j in range(n*n):
            total += 1
    return total

def sum3(n):
    # complexity is O(n)
    total = 0
    for i in range(n):
        for j in range(i*i):
            if (j % i) == 0:
                for k in range(j):
                    total += 1
    return total

def main():
    n = 100
    print(sum3(n))

main()