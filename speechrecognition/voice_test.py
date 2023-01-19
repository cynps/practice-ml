from os import path
import speech_recognition as sr

# variant 
rangeparam = 13

r = sr.Recognizer()

try:
  for i in range(rangeparam):
    f = open("dist/output/result.txt", "a")

    audio_file = path.join(path.dirname(path.realpath(__file__)), "dist/output/output_{}.wav".format(i))
    print(audio_file)

    with sr.AudioFile(audio_file) as source:
      audio = r.record(source)

    text = r.recognize_google(audio, language='ja-JP')
    f.write(text)
    f.write("\r\n")
    
    f.close()

  f = open("dist/output/result.txt", "a")
  f.write("\r\n")
  f.close()

except sr.UnknownValueError:
  print("error")
except sr.RequestError as e:
  print("request error; {0}".format(e))
