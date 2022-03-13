import sys

def sol(arr, N):
    count3 = 0
    count5 = 0
    count15 = 0
    for num in arr:
        if num % 15 == 0:
            count15+=1
            continue
        elif num % 5 == 0:
            count5 += 1
            continue
        elif num % 3 == 0:
            count3 += 1
            continue
    if count15>0: 
        if count15+count3 >= count5:
            return "ALICE"
        else:
            return "BOB"
    else:
        if count3 <= count5:
            return "BOB"


if __name__ == '__main__':
    N = int(input())
    arr = [int(i) for i in sys.stdin.readline().strip().split()]
    print(sol(arr, N))