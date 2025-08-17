
numbers = [12, 5, 7, 3, 19, -4, 8]

smallest = numbers[0]  
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)
