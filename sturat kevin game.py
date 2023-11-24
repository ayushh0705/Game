def minion_game(string):
    vowel = "AEIOU"
    length = len(string)
    kevin = 0
    stuart = 0

    for i in range(length):
        if string[i] in vowel:
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)