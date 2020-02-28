# start from 1 to 1000, quantity of 17 times and sum of them.


q = 0
s = 0
for n in range(1,1001):
    if n%17 == 0:
        q += 1
        s += n

print('quantity of 17 times: {}, sum of 17 times: {}'.format(q, s))

    
