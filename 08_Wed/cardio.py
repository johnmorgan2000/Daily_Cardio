def main():
    example = [1,0,-1,-2,1,0,1,0]

def solution1(list):
    elevation = 0
    has_been_above = True
    below_counter = 0

    for i in list:
        elevation += i
        if elevation < 0 and has_been_above == True:
            below_counter += 1
            has_been_above = False
        elif elevation >= 0 and has_been_above != True:
            has_been_above = True
    return below_counter



def test():
    example = [1,0,-1,-2,1,0,1,0]
    answer = solution1(example)
    if 1 == answer:
        print("Passed")
    else:
        print("Failed")

def solution2():
    return

if __name__ == "__main__":
    test()
