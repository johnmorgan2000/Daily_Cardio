def main():
    input1 = input("Num 1: ")
    solution1(int(input1))

    input2 = input("Num 2: ")

    solution2(int(input2))

def solution1(input):
    for i in range(1, input):
        if (is_factor(i, input)):
            print(str(i) + " is a factor of " + str(input))
        else:
            print(str(i) + " is NOT a factor of " + str(input))
            
def solution2(input):
    i = 1
    while i < input:
        if (is_factor(i, input)):
            print(str(i) + " is a factor of " + str(input))
        else:
            print(str(i) + " is NOT a factor of " + str(input))
        i += 1

def is_factor(num, input):
    if input % num == 0:
        return True
    return False


if __name__ == "__main__":
    main()
