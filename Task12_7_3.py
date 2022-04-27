per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = []
print('Годовые ставки банков:')
print('TKB:', per_cent ['TKB'], 'SKB:', per_cent ['SKB'], 'VTB:', per_cent ['VTB'], 'SBER:', per_cent ['SBER'])
money = int(input("Ведите сумму вклада:"))
for key in per_cent:
    per_cent[key] = int(money * per_cent[key] /100)
    deposit.append(per_cent[key])
print("Доходность по каждому из банков:", deposit)
print('Максимальная доходность:', max(deposit))