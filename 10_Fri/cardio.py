def main():
    magazine = "Hello World"
    message = "He old"
    print(solution2(magazine, message))

def solution1(magazine, message):
    magazine_letters = list(magazine)
    message_letters = list(message)
    for letter in message_letters:
        if letter in magazine_letters and letter != " ":
            magazine_letters.remove(letter)
            continue
        elif letter == " ":
            continue
        else:
            return False 
    return True
        
def solution2(magazine, message):
    magazine_letters = list(magazine)
    message_letters = list(message)
    i = 0
    while i < len(message_letters):
        if message_letters[i] in magazine_letters and message_letters[i] != " ":
            magazine_letters.remove(message_letters[i])
            i+=1
            continue
        elif message_letters[i] == " ":
            i+=1
            continue
        else:
            return False 
        
    return True
    
        

if __name__ == "__main__":
    main();
