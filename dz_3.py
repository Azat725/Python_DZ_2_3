operator = input('Введите своего оператора /n1 - билайн /n2 - мтс /n3 - мегафон /n4 - теле2 ')

cost = float(input('Введите стоимость разгвовра: '))
minute = float(input('Введите количество минут: '))

if operator == 'билайн':
    total = cost * minute
    print('За {minute} количество минут вы заплатите {total} рублей')
elif operator == 'мтс':
    total = cost * minute
    print('За {minute} количество минут вы заплатите {total} рублей')
elif operator == 'мегафон':
    total = cost * minute
    print('За {minute} количество минут вы заплатите {total} рублей')
elif operator == 'теле2':
    total = cost * minute
    print('За {minute} количество минут вы заплатите {total} рублей')
else:
    print('Ошибка, попробуйте еще раз')