
def main():
    response = input("String: ")
    solution2(response)

def solution1(input):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in input:
        multi = alpha.index(letter.lower())
        i=0;
        new_string = ""
        while i < multi:
            new_string += letter
            i += 1
        print(new_string);

def solution2(input):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    j = 0;
    while j < len(input):
        multi = alpha.index(input[j].lower())
        i=0;
        new_string = ""
        while i < multi:
            new_string += input[j]
            i += 1
        print(new_string);
        j += 1

if __name__ == "__main__":
    main();
