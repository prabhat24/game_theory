def cnt_set_bit(num):
	cnt = 0
	while num != 0:
		cnt+=1
		num = num & num - 1
	return cnt

def check_prime(num):
	i = 2
	while i * i <= num:
		if num % i == 0:
			return False
		i += 1
	return True

def sol(num):
	if num == 1:
		return "BOB"
	if num == 2:
		return "ALICE"
	if num & 1 == 0:
		# even
		if cnt_set_bit(num) == 1:
			return "BOB"
		elif num % 4 == 0:
			print("26")
			return "ALICE"
		new_num = num / 2
		if check_prime(new_num):
			return "BOB"
		else:
			return "ALICE"
	else:
		return "ALICE"


if __name__ == '__main__':
	t = int(input())
	cases = [0] * t 
	for i in range(t):
		cases[i] = int(input().strip())
	for num in cases:
		print(sol(num))