#Introduction to Computation and Programming Using Python
#完全立方の立方根を求める2(P29)
#Find_the_cube_root_of_a_perfect_cube2(P29)

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
