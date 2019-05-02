def main():
    solution1(15)

def solution1(num):
    for i in range(1, num + 1):
        if i % 3 ==0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
