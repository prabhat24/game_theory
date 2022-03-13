def sol(n):
    x = 2
    # loss state can be predicticted by using formula = n%(x+1)
    # where x is the max num of coins player can pick
    # eg in case where player can pick 1,2,3 or 4 coins, x = 5
    ans = True if n%(x+1)>0 else False
    return ans


def sol_m2(n, allowed_coins, dp):
    if n==0:
        dp[n] = False
        return False
    if n in allowed_coins:
        dp[n] = True
        return True
    if dp[n]:
        return dp[n] 
    for coin in allowed_coins:
        if n-coin>0:
            if sol_m2(n-coin, allowed_coins, dp) == False:
                dp[n] = True
                return dp[n]
    dp[n] = False
    print(dp)
    return dp[n]

if __name__ == '__main__':
    # n = input()
    # if sol(int(n)):
    #     print("ALICE")
    # else:
    #     print("BOB")
    dp = [None] * (11+1)
    print(sol_m2(11, [1,3,4], dp))