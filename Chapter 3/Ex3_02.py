"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
"""
hours = input('Enter Hours:')
try :
    hours = float(hours)
except :
    print('Error, please enter numeric input')
    quit ()
rate = input('Enter Rate: ')
try :
    rate = float(rate)
except :
    print('Error, please enter numeric input')
    quit()

if hours > 40 :
    ex_hours = hours - 40 #Extra hours
    ex_pay = ex_hours * rate * 1.5 #Extra payment
    n_pay = 40 * rate #Normal payment
    sum_pay = n_pay + ex_pay
    print('Pay:',sum_pay)
else :
    pay = hours * rate
    print('Pay:',pay)
