"""
Домашнее задание №1
Исключения: приведение типов
* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
             print(price)
        else:
            print(price - (price * discount / 100))
    except(ValueError,TypeError):
        print('Некорректные данные')
    

if __name__ == "__main__":
    discounted(100, 2)
    discounted(100, "3")
    discounted("100", "4.5")
    discounted("five", 5)
    discounted("сто", "десять")
    discounted(100.0, 5, "10")