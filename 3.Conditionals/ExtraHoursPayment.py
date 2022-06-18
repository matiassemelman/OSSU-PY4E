# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('How many hours you worked?'))
normalRate = 2.75
extraRate = normalRate * 1.5

normalHoursPay = hours * normalRate if hours <= 40 else 40 * normalRate

extraHoursPay = (hours - 40) * extraRate if hours > 40 else 0

totalPay = normalHoursPay + extraHoursPay

print(str(totalPay))
