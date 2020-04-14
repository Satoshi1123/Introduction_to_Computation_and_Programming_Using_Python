#Introduction to Computation and Programming Using Python
#整数の2乗を地道に求める(P22)
#Find_the_square_of_an_integer_steadily(P22)

x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))
