for number in range(1, 25):
    if number % 3 == 0:
        print(number)
        print([number for number in range(1, 25) if number % 3 == 0])