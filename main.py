# Create dictionary for encoding
char_to_dots = {
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
    ' ': ' ',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '&': '.-...',
    "'": '.----.',
    '@': '.--.-.',
    ')': '-.--.-',
    '(': '-.--.',
    ':': '---...',
    ',': '--..--',
    '=': '-...-',
    '!': '-.-.--',
    '.': '.-.-.-',
    '-': '-....-',
    '+': '.-.-.',
    '"': '.-..-.',
    '?': '..--..',
    '/': '-..-.'
}

# Create dictionary, swapping values
dots_to_char = {v: k for k, v in char_to_dots.items()}

# Function to encode
def encode_morse(message):
    message = message.upper()
    output = " ".join(char_to_dots.get(x, 0) for x in message)
    return output

# Function to decode
def decode_morse(message):
    message = message.split(' ')
    output = " ".join(str(dots_to_char.get(x, '')) for x in message)
    return output

# Tests to encode and decode based on user input
if __name__ == '__main__':
    user_input = input("Enter text to be encoded: ")
    encoded_output = encode_morse(user_input)
    print("Encoded output is: ", encoded_output)

    user_input = input("Enter text to be decoded: ")
    decoded_output = decode_morse(user_input)
    print("Decoded output is: ", decoded_output)
