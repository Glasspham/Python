'''
n =  5
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
'''
n = int(input())
print('n = ', n)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end = ' ')
        i += 1
    print()