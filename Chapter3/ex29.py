#Introduction to Computation and Programming Using Python
#指練習(P29)

total = 0
s = '1.23,2.4,3.123'
s_list = s.split(',')

s_int = [float(sf) for sf in s_list]
for x in s_int:
    total = total + x
print(total)
