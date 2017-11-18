#1 Import dependencies
import speech_recognition as sr

#2 Call function recognizer() from SpeechRecognition
r = sr.Recognizer()

#3 Use and Listen from microphone as source
with sr.Microphone() as source:
	#4 Indication to start your speech, you can change the text as your preference
	print ('Say something')
	#5 Store the audio in variable
	audio = r.listen(source)

try:
	#6 Use recognize_google function to print audio to text
	print('Google thinks you said: \n' + r.recognize_google(audio)) 

	#7 Exception
except Exception as Ex:
	print(Ex)