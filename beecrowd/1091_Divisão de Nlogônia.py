k = int(input())
while k != 0:
        m, n = map(int, input().split())
        for _ in range(k):
            x, y = map(int,input().split())
            if m == x or n == y:
                print('divisa')
            elif x < m and y > n:
                print('NO')
            elif x < m and y < n:
                print('SO')
            elif x > m and y > n:
                print('NE')
            elif x > m and y < n:
                print('SE')
        k = int(input())