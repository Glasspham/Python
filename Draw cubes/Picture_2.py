'''
n =  5            n = 6
* * * * *         * * * * * *
    *             * * * * * *
    *                 * *
    *                 * *
    *                 * *
                      * *
'''
n = int(input())
print('n = ', n)
if n % 2 != 0:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == (n + 1) / 2:
                print('* ',end = '')
            else:
                print('  ',end = '')
        print()
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == 2 or j == n / 2 or j == (n / 2) + 1:
                print('* ',end = '')
            else:
                print('  ',end = '')
        print()