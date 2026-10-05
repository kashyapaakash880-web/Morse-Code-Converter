MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    " ": "/"
}


def text_to_morse_code(text):

    result_text = []

    for char in text.upper():
        if char in MORSE_CODE:
            result_text.append(MORSE_CODE[char])
        else:
            result_text.append("Please Entry English Alphabet ")

    return " ".join(result_text)


def morse_to_text(code):

    reversed_code = {
        value : key for (key, value) in MORSE_CODE.items()
    }

    code_result = []

    for char in code.split(" "):

        if char in reversed_code:
            code_result.append(reversed_code[char])

        else:
            code_result.append("Please Entry the Morse Code eg. --... --... / .- .- -.- ... ....")


    return " ".join(code_result)


while True:
    print("\n===== MORSE CODE CONVERTER =====")
    print("=== Welcome to the place where you convert text into Morse code or Morse code into text ===")
    print("=== Your Option are : ===")
    print("1. Text → Morse")
    print("2. Morse → Text")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":

        text_msg = input("Enter your text: ")
        result_1 = text_to_morse_code(text_msg)
        print(f"Morse Code: {result_1}")

    elif choice == "2":

        code_msg = input("Enter your Morse Code: ")
        result_2 = morse_to_text(code_msg)
        print(f"Text Message : {result_2}")


    elif choice == "3":
        print("Thank you for using Morse Code Converter Hope You have good day ahead 😎🙌")
        break

    else:
        print("Please enter a valid option 😥")








