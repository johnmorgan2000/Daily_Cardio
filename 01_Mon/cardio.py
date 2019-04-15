
def iterator1(input):
    i = 1
    while i < input:
        print(str(i) + ":" + getType(i))
        i += 1

def interator2(input):
    for i in range(input):
        print(str(i) + ":" + getType(i))


def getType(input):
    if input % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    input1 = input("Num 1:")
    iterator1(int(input1))

    input2 = input("Num 2:")
    iterator1(int(input2))


if __name__ == "__main__":
    main()
