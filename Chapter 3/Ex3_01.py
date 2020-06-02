"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate: '))
if hours > 40 :
    ex_hours = hours - 40 #Extra hours
    ex_pay = ex_hours * rate * 1.5 #Extra payment
    n_pay = 40 * rate #Normal payment
    sum_pay = n_pay + ex_pay
    print('Pay:',sum_pay)
else :
    pay = hours * rate
    print('Pay:',pay)
