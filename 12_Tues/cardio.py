import math

def main():
    solution1("a", 50)
    solution1("ab", 60)
    solution1("aba", 5)
    solution1("c", 100000000000000000000000000000000000)
    solution1("", 1)
    solution1("", 0)
    solution1("ab", 1)
    return


def solution1(repeater, char_num):
    a_count = repeater.count("a")
    

  
    if len(repeater) > 0 and repeater.count("a") > 0:
        remainder = char_num % len(repeater)
        answer = (char_num // len(repeater)) * repeater.count("a") + repeater[:remainder].count("a")
    else:
        answer = 0

    print(answer)


    # num_a_in_string = repeater.count("a")
    # len_of_repeater = len(repeater)

    # if len_of_repeater > 0:
    #     answer = math.floor(num_a_in_string * (char_num / len_of_repeater))
    # else:
    #     answer = 0

    # print(answer)


if __name__ == "__main__":
    main()
