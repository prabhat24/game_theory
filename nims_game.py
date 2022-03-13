import sys

def nims_game(piles, coins):
	xor_sum = 0
	for p in range(0, piles):
		xor_sum = xor_sum ^ coins[p]
	if xor_sum == 0:
		return 'BOB'
	else:
		return "ALICE"



if __name__ == '__main__':
	piles = int(input())
	coins = []
	coins = sys.stdin.readline().strip()
	coins = coins.split()
	coins = [int(coin) for coin in coins]
	print(nims_game(piles, coins))