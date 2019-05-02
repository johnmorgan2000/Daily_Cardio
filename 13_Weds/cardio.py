def main():
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    input_list1 = [[2,2,2],[1,1,1], [1,2,3]]
    solution1(input_list);
    return

def solution1(input_list):
    x= 0
    y= 0
    sub_squares_subs = []

    for y in range(0, len(input_list) -1):
        for x in range(0, len(input_list[y])-1):
                sub_square = [
                    input_list[y][x],
                    input_list[y][x + 1],
                    input_list[y+1][x],
                    input_list[y+1][x+1]
                ]
                sub_squares_subs.append(sum(sub_square))
    print(max(sub_squares_subs))

if __name__ == "__main__":
    main();
