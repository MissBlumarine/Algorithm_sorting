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

def heapify(nums, heap_size, root_index):
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


# Сортировка слиянием

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_lenght, right_list_leght = len(left_list), len(right_list)

    for _ in range(left_list_lenght + right_list_leght):
        if left_list_index < left_list_lenght and right_list_index < right_list_leght:
            # сравниваем первые элементы в начале каждого списка
            # если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_lenght:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        # если достигнут конец правого списка, элементы левого списка
        # добавляем в конец результирующего списка
        elif right_list_index == right_list_leght:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # возвращаем список, если он состоит из 1-го элемента
    if len(nums) <= 1:
        return nums

    # Для того, чтобы найти середину списка, используем деление без остатка
    # индексы должны быть int
    mid = len(nums) // 2

    # сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


# random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
# random_list_of_nums = merge_sort(random_list_of_nums)
# print(random_list_of_nums)


# Быстрая сортировка

def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j

        # если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом J (справа от опорного) --> меняем их местами
        nums[i], nums[j] = nums[j], nums[j]


def quick_sort(nums):
    # создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


random_list_of_nums = [1, 2, 0, 3, 5, 6, 8, 9, 7, 11, 34, 12, 13, 15]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
