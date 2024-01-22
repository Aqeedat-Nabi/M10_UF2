def calcul_sq(number):
    return number ** 2

def add_to_list(func, input_list):
    output_list = [func(item) for item in input_list]
    return output_list
