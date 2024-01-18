def Piramide(n):
    for i in range(1, n+1): 
        lineas = ' ' * (n - i)
        asteriscos = '* ' * i
        print(lineas + asteriscos)
print('introduce numero entero de n :')
n = int(input().strip())
Piramide(n)