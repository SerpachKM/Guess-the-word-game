import random

def pop():

    print('Добро пажаловать в Игру угадай слово\n')

    sv = ['да', 'потому', 'сторона', 'думать', 'сделать', 'страна', 'жить', 'мир', 'последний', 'случай', 'голова',
              'мандарин', 'яблоко', 'груша', 'виноград', 'апельсин', 'манго']
    random_index = random.randint(0, len(sv) - 1)
    n = sv[random_index]

    while n:

        random_index = random.randint(0, len(n) - 1)
        h = n[random_index]

        print('В этом слове - ',len(n),'\n')
        c = (input('От гадайте слово - ',))

        if c == n:
            c = False
            print('\nПоздравляю вы молодец')
            break
        if c < n:
            c = False
            print('\nВы не угадали попробуйте еще раз')
            print('\nПодсказка в этом слове есть буква: ', h)
            continue
        if c > n:
            c = False
            print('\nПодсказка в этом слове есть буква: ', h)
            print('\nВы не угадали попробуйте еще раз')
            continue

ans = 'да'
while ans == 'да':
    pop()
    ans = (input('Хочешь сыграть снова? (да или нет)?: '))

