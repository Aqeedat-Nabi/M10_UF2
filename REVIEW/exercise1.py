print(" Hello World ! ")


def range(num1, num2):
    start_num = min(num1, num2)
    end_num = max(num1, num2)

    numbers_in_range = list(range(start_num, end_num + 1))

    print(f"Numbers between {start_num} and {end_num}: {numbers_in_range}")

    sum_of_numbers = sum(numbers_in_range)
    print(f"Sum of the numbers: {sum_of_numbers}")

    return numbers_in_range, sum_of_numbers
