from Module4.Module_4.sortfunc import buble_sort, selection_sort

data_1 = list(map(int, input('Введите список:').split()))  # 1 2 3 4 5
data_2 = list(map(int, input('Введите список:').split()))
data_3 = list(map(int, input('Введите список:').split()))

buble_sort(data_1)
selection_sort(data_2)

print('Пузырьковая сортировка:', data_1)
print('Сортировка:', data_2)