import sys

def sol(A, B, n, m):
	A.sort()
	B.sort()
	i = 0
	j = 0
	while A[i] == 0:
		i+=1
	while B[j] == 0:
		j+=1
	while i < n and j < m:
		if A[i] == B[j]:
			i+=1
			j+=1
		else:
			return "ALICE"

	if i == n and j == m:
		return "BOB"
	else:
		return "ALICE"


if __name__ == '__main__':
	n, m = [int(i) for i in sys.stdin.readline().strip().split()]
	A = [int(i) for i in sys.stdin.readline().strip().split()]
	B = [int(i) for i in sys.stdin.readline().strip().split()]
	print(sol(A, B, n, m))