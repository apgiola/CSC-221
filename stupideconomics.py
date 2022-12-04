price = [0, 20, 40, 60, 80, 100, 120]
qsupply = [0, 20, 40, 60, 80, 100, 120]
total1 = 0
total2 = 0
for i in range(len(price)):
    total1 = (price[i] - 20) * qsupply[i]
    total2 += total1
print(total2)