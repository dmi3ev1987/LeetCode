class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(
            format(int(date_part), 'b') for date_part in date.split('-')
        )
