max =  0
min = 0

while True :
    num  = input('Enter a number:')
    if num == 'done':
        break
    try :
        num = float(num)
    except :
        print('Invalid input')
        continue
    if num > max :
        max = num
    if num < min :
        min = num

print('Maximum:',max,'Minimum:', min)
