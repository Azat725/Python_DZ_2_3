num = int(input('Введите число: '))
deg = int(input('Введите в какую степень возвести чило от 0 до 7:'))

comp = num ** deg 

print(comp)

if deg < 0: 
    print('Введите степень от 0 до 7')
elif deg > 7:
    print('Введите степень от 0 до 7')