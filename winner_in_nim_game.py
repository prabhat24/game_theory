import sys

def sol(arr, n):
    xor_sum = 0 
    for i in arr:
        xor_sum += i
    if xor_sum == 0:
        return "Alice"
    else:
        if n % 2 == 0:
            return "Alice"
        else:
            return "Bob"


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in sys.stdin.readline().strip().split()]
    print(sol(arr, n))