class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        find_even_index = [
            index for index in range(len(digits)) if digits[index] % 2 == 0
        ]
        result = []
        while find_even_index:
            even_index = find_even_index.pop()
            for index in range(len(digits)):
                if index == even_index:
                    continue
                copy_digits = digits.copy()
                if even_index > index:
                    temp_result = [str(copy_digits.pop(even_index))]
                    temp_result.append(str(copy_digits.pop(index)))
                else:
                    temp_result = [str(copy_digits.pop(index))]
                    temp_result.append(str((copy_digits.pop(even_index))))
                    temp_result = temp_result[::-1]
                if temp_result[-1] == "0":
                    continue
                for number in copy_digits:
                    list_to_append = temp_result.copy()
                    list_to_append.insert(1, str(number))
                    list_to_append = list_to_append[::-1]
                    result.append(int("".join(list_to_append)))

        return sorted(set(result))
