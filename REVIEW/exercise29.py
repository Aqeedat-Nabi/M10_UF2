def show_range(num1, num2):
    start_num = min(num1, num2)
    end_num = max(num1, num2)

    numbers_in_range = list(range(start_num, end_num + 1))

    sum_of_numbers = sum(numbers_in_range)

    return numbers_in_range, sum_of_numbers