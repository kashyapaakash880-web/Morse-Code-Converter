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
    """Convert normal text into Morse code."""

    text = text.upper()

    invalid_characters = []

    for char in text:
        if char not in MORSE_CODE:
            invalid_characters.append(char)

    if invalid_characters:
        return f"Invalid character(s): {' '.join(invalid_characters)}"

    result = []

    for char in text:
        result.append(MORSE_CODE[char])

    return " ".join(result)


def morse_to_text(code):
    """Convert Morse code into normal text."""

    reversed_code = {
        value: key
        for key, value in MORSE_CODE.items()
        if key != " "
    }

    # Separate words using /
    words = code.strip().split(" / ")

    decoded_words = []

    for word in words:

        letters = word.split()

        decoded_word = []

        for letter in letters:

            if letter in reversed_code:
                decoded_word.append(reversed_code[letter])

            else:
                return f"Invalid Morse Code: {letter}"

        decoded_words.append("".join(decoded_word))

    return " ".join(decoded_words)


def main():

    while True:

        print("\n===== MORSE CODE CONVERTER =====")
        print("Welcome to the place where you can convert text into Morse code")
        print("or Morse code into text.")

        print("\nYour Options:")
        print("1. Text → Morse")
        print("2. Morse → Text")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            text_msg = input("\nEnter your text: ")

            result = text_to_morse_code(text_msg)

            print(f"\nMorse Code: {result}")

        elif choice == "2":

            code_msg = input("\nEnter your Morse Code: ")

            result = morse_to_text(code_msg)

            print(f"\nText: {result}")

        elif choice == "3":

            print(
                "\nThank you for using Morse Code Converter! "
                "Hope you have a good day ahead 😎🙌"
            )

            break

        else:

            print("\nPlease enter a valid option: 1, 2, or 3.")


if __name__ == "__main__":
    main()
