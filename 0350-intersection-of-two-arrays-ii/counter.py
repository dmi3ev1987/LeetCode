from collections import Counter


def intersect(nums1, nums2):
    counts1 = Counter(nums1)
    counts2 = Counter(nums2)
    result = []

    # Итерируемся по элементам и их частотам в меньшем Counter
    # чтобы потенциально ускорить процесс,
    # если один массив значительно меньше другого
    if len(counts1) > len(counts2):
        counts1, counts2 = (
            counts2,
            counts1,
        )  # Меняем местами, чтобы counts1 был меньше

    for num, count1 in counts1.items():
        if num in counts2:
            # Добавляем элемент минимальное количество раз,
            # которое он встречается в обоих массивах
            count_in_intersection = min(count1, counts2[num])
            result.extend([num] * count_in_intersection)

    return result
