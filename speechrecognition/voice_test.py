from os import path
import speech_recognition as sr

r = sr.Recognizer()

audio_file = path.join(path.dirname(path.realpath(__file__)), "sample.wav")
print(audio_file)

with sr.AudioFile(audio_file) as source:
  audio = r.record(source)

try:
  text = r.recognize_google(audio, language='ja-JP')
  print(text)
except sr.UnknownValueError:
  print("error")
except sr.RequestError as e:
  print("request error; {0}".format(e))
