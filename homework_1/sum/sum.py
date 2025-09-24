def max_even_sum(numbers):
    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return total_sum

    min_odd = None
    for num in numbers:
        if num % 2 == 1:
            if min_odd is None or num < min_odd:
                min_odd = num
                
    if min_odd is not None:
        return total_sum - min_odd
    else:
        return 0 
