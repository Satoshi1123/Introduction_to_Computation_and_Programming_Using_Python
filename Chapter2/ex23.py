#Introduction_to_Computation_and_Programming_Using_Python
#指練習
#ex23.py(p23)

numXs = int(input('How many times should I print the letter X? '))

toPrint = ''
while numXs > 0:
    toPrint+='X'
    numXs -=1

print(toPrint)
