#Introduction to Computation and Programming Using Python
#ニュートン-ラフソン法の実装(P36-P37)
#Newton-Raphson method implementation(P36-P37)

#平方根を求めるニュートン-ラフソン法
#x**2 - 24 = 0で誤差がepsilon以下になるxを求める

epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
