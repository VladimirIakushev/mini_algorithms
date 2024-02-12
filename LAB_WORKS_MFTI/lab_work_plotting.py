import numpy as np
import matplotlib.pyplot as plt
# import requests
# from pprint import pprint


def exercise_1():
    ''' \n
    Запишите выражение, заданное формулой, в виде, подходящем для языка Python
    и найдите его значения в точках 1, 10, 1000 \n'''
    range_x = (1, 10, 1000)
    for x in range_x:
        y = np.log((np.e ** (1 / (np.sin(x) + 1))) /
                   ((5 / 4) + (1 / (x ** 2)))) / np.log(1 + (x ** 2))
        print(f'В точке {x} значение функции равно {y}')


def exercise_2():
    '''Постройте график функции'''
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, x*x - x - 6)
    plt.show()


def exercise_3():
    '''Постройте график функции'''
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, np.log((x ** 2 + 1) * np.exp(-abs(x) / 10)) /
             np.log(1 / np.sin(x) ** 2))
    plt.show()


def exercise_4():
    '''Построить график функции, введенной с клавиатуры'''
    x = np.arange(-10, 10.01, 0.01)
    func = input()
    with plt.xkcd():
        plt.plot(x, eval(func))
        plt.show()


def exercise_5():
    # response = requests.get(
    # 'https://cs.mipt.ru/python/lessons/lab1.html#toc-entry-9'
    # )
    # pprint(response.text)
    print('Задание располодежено по ссылке:')
    print('https://cs.mipt.ru/python/lessons/lab1.html#toc-entry-9')


def exercise_6():
    print('Задание располодежено по ссылке:')
    print('https://cs.mipt.ru/python/lessons/lab1.html#toc-entry-9')
    print('Если, конечно, знать, что такое функция Вейштрасса')
    print('И зачем она нужна...')


def main():
    print('Введите номер упражнения:')
    number = int(input())
    if number <= 6:
        func_name = f'exercise_{number}'
        eval(func_name)()
    else:
        print('Переходим к следующему упражнению.')


main()
