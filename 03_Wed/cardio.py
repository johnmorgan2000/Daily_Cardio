def main():
    input1 = input("String 1: ");
    input2 = input("String 2: ");
    # solution1(input1, input2)
    solution2(input1, input2)

def solution1(input1, input2):
    new_string = ""
    for i in range(0, len(input1)):
        if input1[i] == input2[i]:
            new_string += input1[i]
        else:
            new_string += "."
    print(new_string)

def solution2(input1, input2):
    new_string = ""
    i = 0
    while i < len(input1):
        if input1[i] == input2[i]:
            new_string += input1[i]
        else:
            new_string += "."
        i +=1
    print(new_string)

        

    
def mapHandler(new_string,x):
    new_string = "";
    new_string += x
    return new_string


if __name__ == "__main__":
    main();
