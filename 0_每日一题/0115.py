class Solution:
    def save_week(self, monday_money):
        return int((monday_money + monday_money + 6) * 7 / 2)

    def totalMoney(self, n: int) -> int:
        money = 0
        weeks = n // 7
        days = n % 7
        for w in range(weeks):
            money += self.save_week(w + 1)
        m = weeks + 1
        for d in range(days):
            money += m
            m += 1
        return money


if __name__ == '__main__':
    n = 4
    money = Solution().totalMoney(n)
    print(money)
