salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


def define_cash(spend, salary, months):
    need_money = 0
    for i in range(months):
        if i > 0:
            spend *= (1 + increase)
        need_money += -salary + spend
    return need_money


need_money = define_cash(spend, salary, months)
print(round(need_money))
