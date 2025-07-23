def move_zeroes(nums):
    # Указатель для отслеживания позиции следующего ненулевого элемента
    insert_pos = 0

    # Перебираем массив. Если элемент не ноль, помещаем его на позицию insert_pos
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    # Все ненулевые элементы теперь в начале массива до позиции insert_pos.
    # Заполняем оставшуюся часть массива нулями.
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
