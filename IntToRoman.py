#enum
class Solution:
    def intToRoman(self, num: int) -> str:
        to_r = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
       
        }

        roman = ''

        for i in to_r:
            while i <= num:
                num -= i
                roman += to_r[i]

        return roman
