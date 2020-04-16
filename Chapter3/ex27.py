#Introduction to Computation and Programming Using Python
#指練習(P27)

x = int(input('Enter a positive integer: '))

root = 1
pwr = 1
count = 0

while root**pwr <= x:
    if root**pwr < x:
        pwr += 1
    elif root**pwr == x:
        print(root, pwr)
        count += 1
        pwr += 1
    if pwr > 6 or root**pwr > x:
        root += 1
        pwr = 1

if count == 0:
    print('no pair')
