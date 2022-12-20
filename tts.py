import pyttsx3
import morse


def speak_morse(message):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    message = message.upper()
    output = ""
    for x in message:
        if x in morse.char_to_dots:
            value = str(morse.char_to_dots.get(x, 0))
            output += value + " "
            value = value.replace(".", " dot")
            value = value.replace("-", " dash")
            # Speak the encoded character
            engine.say(value, 0.25)
            # Pause for 0.5 seconds
            engine.runAndWait()
    print(output)
