import datetime
import json
# from random import randint

# Список, где хранятся все числа
res = []

# Список файлов
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


# for file in files:
#     # Запись рандомных чисел в файлы
#     for _ in range(100_000):
#         res.append(randint(0, 10_000))
#     with open(file, 'w') as f:
#         json.dump(res, f)
#     # Обнуляем список для следующего файла
#     res = []


def main():
    # Словарь, куда всё будем складывать
    res_to_count = []
    start = datetime.datetime.now()
    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            # объединение списков через extend
            res_to_count.extend(data)
            end = datetime.datetime.now()
    return end - start


time_calc = []
for i in range(100):
    time_calc.append(main())
print(sum([calc.microseconds for calc in time_calc]) / len(time_calc)) # 29139.4
