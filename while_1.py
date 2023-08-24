num = 1
sum = 0
#print(f'{num}  ', end='')
while num <= 10:
    sum = sum + num
    if num != 10:
        print(f' {num} + ', end='')
    else:
        print(f'{num} ', end='')
    num = num + 1

print(f'= {sum}')
