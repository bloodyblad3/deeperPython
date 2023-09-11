names = ["John", "Harland", "Charlie"]
stakes = [100, 200, 500]
bonuses = ["10.25%", "5.5%", "15%"]

result = {name: stake * (float(bonus.strip('%')) / 100) for name, stake, bonus in zip(names, stakes, bonuses)}

print(result)