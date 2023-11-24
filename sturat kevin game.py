def minion_game(string):
    # Define the vowels
    vowels = "AEIOU"
    
    # Get the length of the input string
    length = len(string)
    
    # Initialize scores for Kevin and Stuart
    kevin_score = 0
    stuart_score = 0

    # Iterate through each character in the string
    for i in range(length):
        # Check if the character is a vowel
        if string[i] in vowels:
            # If it's a vowel, increment Kevin's score by the number of substrings
            kevin_score += length - i
        else:
            # If it's a consonant, increment Stuart's score by the number of substrings
            stuart_score += length - i

    # Compare scores and print the result
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == "__main__":
    # Get user input for the string
    s = input("Enter the string: ").upper()
    
    # Call the minion_game function with the input string
    minion_game(s)
