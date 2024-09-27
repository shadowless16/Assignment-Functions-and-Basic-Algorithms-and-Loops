def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [10, 20, 30, 40, 50]
print("Sum of the list:", sum_list(my_list))