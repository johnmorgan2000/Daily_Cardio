def main():
    steps = ["n", "n", "n", "n", "n", "s", "s", "s", "s", "s"]
    steps2 = []
    print(solution(steps2))


def solution(steps):
    x = 0
    y = 0
    if len(steps) == 10:
        for step in steps:
            if step == "n":
                y += 1
            elif step == "s":
                y -= 1
            elif step == "e":
                x += 1
            elif step == "w":
                x -= 1
        return isBackToStart(x, y)
    else:
        return False


def isBackToStart(x, y):
    if x == 0 and y == 0:
        return True
    return False


if __name__ == "__main__":
    main()
