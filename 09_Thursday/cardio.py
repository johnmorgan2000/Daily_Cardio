def main():
    socks = ["s1", "s2", "s2", "s1", "s3", "s1", "s1", "s1"]
    solution1(socks)
    return

def solution1(socks):
    singles = []
    matches = 0

    for sock in socks:
        if sock in singles:
            matches += 1
            singles.remove(sock)
        else:
            singles.append(sock)
    print(matches)

    
        

if __name__ == "__main__":
    main();
