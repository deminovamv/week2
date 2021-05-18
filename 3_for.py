"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def sum_scores(students_scores):
    scores_sum = 0
    for score in students_scores:
        scores_sum += score
    return(scores_sum)


def main():
    list_school = [
        {
            "school_class": "4a",
            "scores": [5, 5, 5, 5, 5]
        },
        {
             "school_class": "5a",
             "scores": [3, 4, 4, 5, 2, 3, 5, 3]
        },
        {
            "school_class": "6a",
            "scores": [3, 4, 4, 5, 2, 4]
        },
        {
            "school_class": "7a",
            "scores": [3, 4, 4, 5, 2, 4, 3, 5, 2]
        },
        {
            "school_class": "8a",
            "scores": [3, 4, 2, 4, 3, 5, 2]
        }
    ]
    scores_sum = 0
    students_scores = 0
    for l in list_school:
        class_scores = sum_scores(l['scores'])
        scores_sum += class_scores
        students_scores += len(l['scores'])
        scores_avg = class_scores / len(l['scores'])
    # print('Сумма оценок в классе:{}'.format(class_scores))
    # count = len(l['scores'])
    # print('Всего учеников в классе:{}'.format(count))
        print("средний балл по {} классу: {:.3f}".format(l['school_class'], scores_avg))
    cores_avg = scores_sum / students_scores
    print("средний балл по всей школе: {:.3f}".format(scores_avg))

    
if __name__ == "__main__":
    main()