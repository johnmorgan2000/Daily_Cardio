def main():
    ex = [1, 2, 11, 1, 1, 2, 2, 2, 2]
    ex_2 = []
    ex_3 = [1, 2]
    ex_4 = [2, 2, 2, 1, 2]
    solution(ex_4)


def solution(l):
    current_streak_item = None
    current_streak_num = 0
    highest_streak_item = None
    highest_streak_num = 0

    if len(l) > 0:
        current_streak_item = l[0]
        highest_streak_item = l[0]
        for i in l:
            if i == current_streak_item:
                current_streak_num += 1
                if current_streak_num > highest_streak_num:
                    highest_streak_num = current_streak_num
                    highest_streak_item = current_streak_item
            else:
                current_streak_item = i
                current_streak_num = 1
    print(highest_streak_item, highest_streak_num)


# def solution2(l):
#     current_streak_tuple = (None, 0)
#     highest_streak_tuple = (None, 0)

#     if len(l) > 0:
#         current_streak_tuple = (l[0],0)
#         highest_streak_tuple = (l[0],0)
#         for i in l:
#             if i == current_streak_tuple[0]:
#                 current_streak_tuple[1] += 1
#                 if current_streak_tuple[1] > highest_streak_tuple[1]:
#                     highest_streak_tuple[1] = current_streak_tuple[1]
#                     highest_streak_tuple[0] = current_streak_tuple[0]
#             else:
#                 current_streak_tuple[0] = i
#                 current_streak_tuple[1] = 1;
#     print(highest_streak_tuple);

if __name__ == "__main__":
    main()
