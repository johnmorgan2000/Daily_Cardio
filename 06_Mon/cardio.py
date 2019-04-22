def main():
    ints = [10, 20, 0]
    solution_2(ints)

def solution_1(ints):
    largest = ints[0]
    smallest = ints[0]

    for i in range(0, len(ints)):
        largest = return_largest(largest, ints[i])
        smallest = return_smallest(smallest, ints[i])
    print(str(largest - smallest))

def solution_2(ints):
    largest = ints[0]
    smallest = ints[0]
    i = 0

    while i < len(ints):
        largest = return_largest(largest, ints[i])
        smallest = return_smallest(smallest, ints[i])
        i+=1
    print(str(largest - smallest))
    

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
