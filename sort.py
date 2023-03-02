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


# random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
# insertion_sort(random_list_of_nums)
# print(random_list_of_nums)


# Сортировка кучей (пирамидальная)

def heapify (nums, heap_size, root_index):
    # создаем вспомогательную функцию для реализации нахождения вершины кучи
    # индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # если левый потомок корня - допустимый индекс, а элемент больше
    # чем текущий наибольший --> обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # аналогично для правого потока
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # если наибольший элемент больше не корневой, они меняются местами
    if root_index != largest:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        # теперь проверяем новый корневой элемент, чтобы убедиться, что он наибольший
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # - создаем MAX HEAP из списка
    # - второй аргумент означает остановку алгоритма перед элементов -1, т.е. перед первым элементом списка
    # - третий аргумент означает повторный проход по списку в обратном направлении,
    #   уменьшая счетчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # переменная корень MAX HEAP в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
# heap_sort(random_list_of_nums)
# print(random_list_of_nums)