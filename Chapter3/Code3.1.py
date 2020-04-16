#Introduction to Computation and Programming Using Python
#完全立方の立方根を求める(P25)
#Find_the_cube_root_of_a_perfect_cube(P25)

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x ,'is', ans)
