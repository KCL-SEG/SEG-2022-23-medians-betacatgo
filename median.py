"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        len = len(numbers)
        if len % 2 == 0:
            print((numbers[len // 2] + numbers[len // 2 - 1]) / 2)
        else:
            print(numbers[len // 2])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
