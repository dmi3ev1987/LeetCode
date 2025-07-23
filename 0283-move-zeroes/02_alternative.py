def move_zeroes_swap(nums):
    left = 0  # Указатель на позицию для следующего ненулевого элемента
    for right in range(len(nums)):
        if nums[right] != 0:
            # Если left и right разные, и nums[left] это ноль, а nums[right] не ноль,
            # то меняем их местами. Это гарантирует, что ненулевые элементы двигаются вперед.
            if left != right:  # Оптимизация: не менять элемент сам с собой
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
