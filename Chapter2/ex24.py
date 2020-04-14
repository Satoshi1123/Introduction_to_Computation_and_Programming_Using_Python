#Introduction_to_Computation_and_Programming_Using_Python
#指練習
#ex24.py(p24)

#if and while only(don't use List or function)
count = 1
maxval = 0
kisuu_count = 0
while count <= 10:
    num = int(input('Enter an int: '))
    count += 1
    if num%2!=0:
        kisuu_count +=1
        if num > maxval:
            maxval = num

if kisuu_count == 0:
    print('No odd number')
else:
    print('Largest odd number: ' , maxval)
