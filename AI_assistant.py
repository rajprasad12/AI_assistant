# speaking the computer
import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) # by defalut the pc has two voices
engine.setProperty('voice',voices[1].id) # it will give the voice of female 

# to set computer to say something
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour) # it will return the time in 0 to 24 hr format
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak("hey raj iam your desktop assistant ruvika, how may i help you")
    
def takecommand(): # it takes the voice input from the user and the returns the output
    r = sr.Recognizer() # it will help to recognise the audio from the user
    with sr.Microphone() as source:
        print('listening...')
        #r.pause_threshold = True
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
    try:
        print('recognising...')
        query = r.recognize_google(audio,language='en-in')
        print("user said:", query)

    except Exception as e:
        print('say that again plese..')
        return 'none'
    return query

if __name__ == "__main__":
    speak('welcome')
    wishme()
    while True:
        query = takecommand().lower()
        # logic to execute tasks
        if 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com') 
        
        elif 'open code' in query:
            codepath ="C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codepath)

        elif 'time' in query:
            strtime = datetime.datetime
            speak('sir the time is',strtime)
        
        elif 'lock pc' in query:
            ctypes.windll.user32.LockWorkStation()
        
        
  
