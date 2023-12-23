num = int(input('Введите число от 1 до 100: '))

if num // 3:
    print('Fizz')
elif num // 5:
    print('Buzz')
elif num // 3 and num // 5:
    print('Fizz Buzz')
elif not num // 3 and not num // 5:
    print(num)
elif num < 1 and num > 100:
    print('Error')
