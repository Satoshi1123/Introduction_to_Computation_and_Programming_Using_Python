#Introduction to Computation and Programming Using Python
#指練習(P37)

print('#########ニュートン-ラフソン法#########')
epsilon = 0.01
k = 24.0
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    print('guess = ', guess)
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess,'\n')

print('#########2分法#########')
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, k)
guess = (high + low)/2.0
while abs(guess**2 - k) >= epsilon:
    print('guess =', guess)
    numGuesses += 1
    if guess**2 < k:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)
