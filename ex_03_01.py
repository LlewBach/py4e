hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
extra_hours = 0

if hours >= 40:
    extra_hours = hours - 40
    pay = 40 * rate + (rate * 1.5 * extra_hours)

else: 
    pay = float(hours * rate)

print(pay)