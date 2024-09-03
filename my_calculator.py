# Import the necessary tools(functions)
from my_calculator_functions import compute_sum_of, compute_difference_of, compute_product_of, compute_division_of



def main():
    number_1 = float(input("Enter number 1: "))
    number_2 = float(input("Enter number 2: "))
    my_sum = compute_sum_of(number_1, number_2)
    print(f"Total: {my_sum}")
    my_diff = compute_difference_of(number_1, number_2)
    print(f"Difference: {my_diff}")
    my_product = compute_product_of(number_1, number_2)
    print(f"Product: {my_product}")
    my_division = compute_division_of(number_1, number_2)
    print(f"Division: {my_division}")
    
    

main()
