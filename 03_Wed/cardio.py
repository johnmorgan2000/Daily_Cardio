def main():
    input1 = input("String 1: ");
    input2 = input("String 2: ");
    # solution1(input1, input2)
    solution2(input1, input2)

def solution1(input1, input2):
    new_string = ""
    maxLength = returnGreaterLength(input1, input2);
    minLength = returnLesserLength(input1, input2);
    for i in range(0, maxLength):
        if i < minLength:
            if input1[i] == input2[i]:
                new_string += input1[i]
            else:
                new_string += "."
        else:
            new_string += "."

    print(new_string)

def solution2(input1, input2):
    new_string = ""
    maxLength = returnGreaterLength(input1, input2);
    minLength = returnLesserLength(input1, input2);
    i = 0
    while i < maxLength:
        if i < minLength:
            if input1[i] == input2[i]:
                new_string += input1[i]
            else:
                new_string += "."
        else:
            new_string += "."
        i +=1
    print(new_string)


def returnGreaterLength(input1, input2):
    if len(input1) > len(input2):
        return len(input1)
    else:
        return len(input2)

def returnLesserLength(input1, input2):
    if len(input1) < len(input2):
        return len(input1)
    else:
        return len(input2)

    
def mapHandler(new_string,x):
    new_string = "";
    new_string += x
    return new_string


if __name__ == "__main__":
    main()

