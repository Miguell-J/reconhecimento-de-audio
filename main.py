import speech_recognition as sr

rec = sr.Recognizer()

# print(sr.Microphone().list_microphone_names())

with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar:")
    rec.pause_threshold = 1.6
    audio = rec.listen(microfone)
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
    except:
        print("Não peguei áudio nenhum")