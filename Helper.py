import math
import random

class Helper:

    @staticmethod
    def choose_different_random_numbers(lower_bound, upper_bound, n, sorted = True):
        """
        This function chooses n different numbers between the interval [lower_bound, upper_bound]
        """
        if lower_bound > upper_bound:
            raise Exception("Lower bound cannot be greater than the upper bound!")
        
        number_of_numbers_in_interval = upper_bound - lower_bound + 1
        
        if n > number_of_numbers_in_interval:
            raise Exception(f"Interval is not large enough to generate {n} different numbers!")
            
        chosen = []
        while len(chosen) < n:
            picked = random.randint(lower_bound, upper_bound)
            if not picked in chosen:
                chosen.append(picked)
        
        if sorted:
            chosen.sort()
        
        return chosen

    @staticmethod
    def find_two_closest_factors(n, random_order = True):
        sqrt = math.sqrt(n)
        if sqrt == int(sqrt):
            return (int(sqrt), int(sqrt))
        
        middle = int(sqrt) # starting point
        while n % middle != 0: # find the lower factor
            middle -= 1
        
        first = middle
        second = n // middle # find the greater factor
        
        if random_order and first != second:
            num = random.randint(0, 1)
            if num == 1:
                first, second = second, first # swap numbers
        
        return (first, second)
    
    @staticmethod
    def base_n_to_decimal(n, number):
        # n: int
        # number: str
        
        result = 0
        counter = len(number) - 1
        for digit in number:
            if int(digit) >= n:
                raise Exception(f"Cannot have digit {digit} at base {n}")
            result += int(digit) * pow(n, counter)
            counter -= 1
        
        return result
    
    @staticmethod
    def decimal_to_base_n(n, number, range_list = None, pad_to = 3):
        # n: int
        # number: int
        
        if n > 10 and range_list is None:
            raise Exception("You must specify a range_list for bases greater than 10!")
        
        if range_list is None:
            range_list = [str(i) for i in range(n)]
        
        result = ""
        while number > 0:
            remainder = number % n
            number = number // n
            result = range_list[remainder] + result
        
        number_of_required_zeros = pad_to - len(result)
        if number_of_required_zeros > 0:
            result = '0' * number_of_required_zeros + result
            
        
        return result
