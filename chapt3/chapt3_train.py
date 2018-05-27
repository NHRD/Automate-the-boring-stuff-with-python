def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

def loops():
    while True:
        try:
            start_num = int(input("Input number:"))
            result = collatz(start_num)
            while result != 1:
                print(int(result))
                result = collatz(result)
            print(int(result))
            return False
        except ValueError:
            print("Input int number.")

loops()