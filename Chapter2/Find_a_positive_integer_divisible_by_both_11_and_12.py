##Introduction to Computation and Programming Using Python
#11と12ともに割り切れる正の整数を見つける(P24)
#Find_a_positive_integer_divisible_by_both_11_and_12.py(P24)

x = 1
while True:
    if x%11==0 and x%12==0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')
