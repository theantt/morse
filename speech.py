import speech_recognition as sr


def recognizeSpeech():
    # Speech recognition initialization
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...\n")
        audio = r.listen(source)

    # Get transcript
    audio = r.recognize_google(audio, show_all='False')['alternative'][0]['transcript'].lower()
    return audio
