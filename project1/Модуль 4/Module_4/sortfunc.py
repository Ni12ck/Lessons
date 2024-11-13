# Создам неотсортированный массив чисел
nums1 = [1, 657, 23, 324, 54, 2, 124, 456]
nums2 = [1, 657, 23, 324, 54, 2, 124, 456]


# Пузырьковая сортировка
def buble_sort(num_list):
    # переменная, которая показывает, произошла ли смена мест во время итерации
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num_list) - 1):
            # Если условно элемент 1 больше элемента 2, то мы их меняем местами
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                # Смена произошла
                swapped = True


buble_sort(nums1)
print(f'Пузырьковая сортировка: {nums1}')


# Сортировка выборкой
def selection_sort(num_list):
    for i in range(len(num_list)):
        # Наименьший элемент в списке
        lowest = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[lowest]:
                lowest = j
            num_list[i], num_list[lowest] = num_list[lowest], num_list[i]


selection_sort(nums2)
print(f'Сортировка выборкой: {nums2}')
