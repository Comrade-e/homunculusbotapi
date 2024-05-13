import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Я вас слушаю")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    query = recognizer.recognize_google(audio, language='ru-RU')
    print("Вы сказали:", query)
    return query.lower()
