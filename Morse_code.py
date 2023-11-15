# Command line program
# Morse Code
LETTERS_TO_MC = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}

# Check user input
def user_input():
    user_code = input("Enter your code (Letters or Numbers): ")
    for char in user_code:
        if char.upper() not in LETTERS_TO_MC.keys():
            print(f'{char} is not in the Morse Code dictionary. Please enter numbers 0-9 or letters A - Z.')
            return user_input() # If user input not found in LETTERS_TO_MC, return user_input()
    return to_morse_code(user_code)  # If found, move on to the next function


# Function to convert user input to the morse code
# Take user_code as input
def to_morse_code(code):
    mc_text = ""
    # Swap each character of user_code with the morse code, add them to string 'mc_text'
    for char in code:
        mc_text += LETTERS_TO_MC[char.upper()]
    print(mc_text)

    # Continue or finish
    # Use while loop for continuing the transforming or stopping the program
    while True:
        user_choice = input('Enter X to view your original text, or C to continue: ').upper()
        if user_choice == "X":
            print(f"Your original input is {code}.")
            # Use a nested while loop to continue the program or stop the program
            while True:
                if_continue = input("Enter C to continue or Q to quit: ").upper()
                if if_continue == "C":
                    return user_input() # Continue the program and return to the first step
                elif if_continue == "Q":
                    print("Bye~")
                    break # Stop the whole program
                else:
                    print("Invalid input. Try again.") # Continue the while loop if input is not 'c' or 'q'
            break # Stop the program
        elif user_choice == "C":
            return user_input() # Continue the program and go back to the first step
        else:
            print("Invalid input.") # Continue the while loop if input is not 'x' or 'c'.

# Call the function to start the program
user_input() 
