import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser           
import os
import smtplib #simple mail transfer protocol


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir.")   

    else:
        speak("Good Evening! Sir.")  

    speak(" Please tell me how may I help you")   
    speak("                     Listening...")    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        #speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.ehlo()
    server.starttls()
    server.login('18kumarshivam@gmail.com', '**********')
    server.sendmail('18kumarshivam@gmail.com', to, content)
    server.quit()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open trending music on youtube' in query:
            webbrowser.open("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open college website' in query:
            webbrowser.open("www.akgec.ac.in")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\shiva\\Music\\Fav'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shivam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kumar2013045@akgec.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry my friend Shivam . I am not able to send this email")  
        elif 'exit' in query:
                    speak("Exiting on terminal, thank you!")
                    break
  
