money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


def gonna_die_in(money_capital, salary, spend, month):
    while True:
        spend = spend * (1 + increase * (month + 1))
        money_capital = money_capital + salary - spend
        if money_capital < 0:
            return month
        else:
            month += 1


month = gonna_die_in(money_capital, salary, spend, month)
print(month)
