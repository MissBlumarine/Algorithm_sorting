# Пузырьковая сортировка

# Это неэффективный алгоритм
# Алгоритм повторяетмся n**2 раз, даже если спиок уже отсортирован
#
# Чтобы сделать его эффективнее, необходимо воспользоваться флагами:
#  - если значения меняются местами --> флаг True
#  - если значения не меняются местами --> флаг False --> алгоритм останавливается


def bubble_sort(nums):
    # уставливаем swapped = True, чтоб алгоритм запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)

# Сортировка вставками

def selection_sort(nums):
    for i in range(len(nums)):
        # исходно считаем наименьшим первый в списке элемент
        lowest_value_index = i
        # этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # самый маленький элемент в списке меняем местами с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
# selection_sort(random_list_of_nums)
# print(random_list_of_nums)


# Сортировка вставками


def insertion_sort(nums):
    # сортировку начинаем со второго элемента, так как первый считается отсортированным
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
