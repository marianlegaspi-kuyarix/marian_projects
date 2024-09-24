import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(f'You said: {command}')

except sr.RequestError:
        print("Could not request results from Google Speech Recognition service; check your network connection.")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except Exception as e:
    print(f"An error occurred: {e}")
