def main():
    num1 = int(input("Num 1: "))
    num2 = int(input("Num 2: "))
    solution2(num1, num2)

def solution1(num1, num2):
    for i in range(1, num2 + 1):
        result = i * num1
        print(str(num1) + " * " + str(i) + " = " + str(result))

def solution2(num1, num2):
    i = 1
    while i <= num2:
        result = i * num1
        print(str(num1) + " * " + str(i) + " = " + str(result))
        i += 1
    

if __name__ == "__main__":
    main()    
