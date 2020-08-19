if __name__ == '__main__':
    def solution(monster, init):
        dp = [init] + monster
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + dp[i] if dp[i - 1] >= dp[i] else dp[i - 1] + gcd(dp[i - 1], dp[i])
        return dp[-1]

    def gcd(a, b):
        a, b = (a, b) if a >= b else (b, a)
        while b:
            a, b = b, a % b
        return a

    print(solution([30, 20, 15, 40, 100], 20))