"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""


def compare(str_one,str_two):
    if type(str_one) is not str and type(str_two) is not str: 
        return('0')
    elif len(str_one) == len(str_two):
        return('1')    
    elif len(str_one) != len(str_two) and len(str_one) > len(str_two) and str_two != 'learn':
        return ('2')
    elif str_one != str_two and str_two == 'learn':
        if len(str_one) > len(str_two):
            return('2,3')
        return('3')
    else:
        return('нет ответа')
def main():
    print(compare('нет ответа','learn'))
    
if __name__ == "__main__":
    main()
