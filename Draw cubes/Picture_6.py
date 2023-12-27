'''
n =  5
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
n = int(input())
print('n = ', n)
for i in range(1,n+1):
    ktao = i
    kc = n - 1
    for j in range(i):
        print(ktao, end = ' ')
        ktao += kc
        kc -= 1
    print()