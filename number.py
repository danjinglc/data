a = []
b = 1

while b < 10:
    c = 1
    while c < b:
        #d = b*c
        print('%d X %d = %2d' %(b,c,b*c),end=' ')
        c = c +1
        print(' ')
    b = b +1
    print(' ')





'''
print("<<九九乘法表>>")
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')
'''

