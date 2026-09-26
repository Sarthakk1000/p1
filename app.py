numbers = input("Enter numbers separated by spaces: ").split()

# Convert each item to an integer
numbers = [int(x) for x in numbers]

sorted_numbers = sorted(numbers)

print("Sorted numbers:", sorted_numbers)