"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
def computepay(hours,rate):
    if hours > 40 :
        ex_hours = hours - 40 #Extra hours
        ex_pay = ex_hours * rate * 1.5 #Extra payment
        n_pay = 40 * rate #Normal payment
        pay = n_pay + ex_pay
        return pay
    else :
        pay = hours * rate
        return pay

def check_float(input):
    try :
        value = float(input)
        return value
    except :
        print('Error, please enter numeric input')
        quit ()

hours = input('Enter Hours:')
hours = check_float(hours)
rate = input('Enter Rate: ')
rate = check_float(rate)

pay = computepay(hours,rate)

print('Pay:',pay)
