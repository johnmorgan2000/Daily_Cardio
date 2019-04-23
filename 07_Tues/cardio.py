def main():
    ints = [1, 1, 0]
    solution_1(ints)

def solution_1(ints):
    ones = 0
    zeros = 0

    for i in ints:
        if i == 1:
            ones += 1
        elif i ==0:
            zeros += 1
    print(ones > zeros)

def solution_2(ints):
    ones = 0
    zeros = 0
    i=0

    while i < len(ints):
        if i == 1:
            ones += 1
        elif i ==0:
            zeros += 1
        i += 1
    print(ones > zeros)
    

def return_largest(largest, current_int):
    if largest < current_int:
        return current_int    
    return largest

def return_smallest(smallest, current_int):
    if smallest > current_int:
        return current_int    
    return smallest

if __name__ == "__main__":
    main()
