import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import webbrowser
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good Morning")
            speak("I am harsh")
            speak("Please tell me how may I help you")    
    elif hour>=12 and hour<18:
            speak("Good Afternoon")
            speak("I am harsh")
            speak("Please tell me how may I help you")    
    else:
            speak("Good Evening") 
            speak("I am harsh")
            speak("Please tell me how may I help you")    


def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
            speak("Listening")
            r.pause_threshold = 1
            audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        return "None"
    return query
    
def dollartoinr():
    speak("Enter the amount in dollars\n")
    dollar=takeCommand()
    inr=int(dollar)*0.014
    speak(inr)
    speak("Rupees")

def inrtodollar():
    speak("Enter the amount in indian rupees\n")
    inr=takeCommand()
    dollar=int(inr)*72.77
    speak(dollar,"  dollar")

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
    
    # Logic for executing tasks based on query
        if "tell me about a monument" or "tell  me about the monument"in query:
            speak("Which one?")
            monument=takeCommand()
            # monument= monument.replace("wikipedia","") 
            results=wikipedia.summary(monument, sentences=3)
            speak(results) 

        elif 'tell me about an actor' or "tell  me about the  actor" in query:
            speak("Which one?")
            actor=takeCommand()
            # actor= actor.replace("wikipedia","") 
            results=wikipedia.summary(actor, sentences=3)
            speak(results) 

        elif 'tell me about a cricketer' or "tell  me about the cricketer" in query:
            speak("Which one?")
            cricketer=takeCommand()
            # cricketer=cricketer.replace("wikipedia","") 
            results=wikipedia.summary(cricketer, sentences=3)
            speak(results)

        elif "tell me about a fruit" or "tell  me about the fruit" in query:
            speak("Which one?")
            fruit=takeCommand()
            # fruit= fruit.replace("wikipedia","") 
            results=wikipedia.summary(fruit, sentences=3)
            speak(results)

        elif "tell me about a film"   or "tell  me about the film"in query:
            speak("Which one?")
            film=takeCommand()
            film= film.replace("wikipedia","") 
            results=wikipedia.summary(film, sentences=3)
            speak(results)

        elif "tell me about a sports"or "tell  me about the sports" in query:
            speak("Which one?")
            sports=takeCommand()
            # sports= sports.replace("wikipedia","") 
            results=wikipedia.summary(sports, sentences=3)
            speak(results)

        elif "tell me about an ancient location" or "tell  me about the ancient location" in query:
            speak("Which one?")
            ancient=takeCommand()
            # ancient= ancient.replace("wikipedia","") 
            results=wikipedia.summary(ancient, sentences=3)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'play' in query:
            speak("Say a number between 1 to 100")
            r = sr.Recognizer()
            my_mic_device = sr.Microphone(device_index=1)
            with my_mic_device as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print("You said")
                print(my_string)
            randomnumber = random.randint(1,10)
            win = False
            Turns =0
            while win==False:
                Turns+=1
                if randomnumber<int(my_string):
                    speak(" smaller Number please!\n")
                    takeCommand()
                elif randomnumber>int(my_string): 
                    speak("higher number please!\n")
                    takeCommand()
                elif randomnumber==int(my_string):
                    speak("Your guess was right!\n")
                    speak("Number of attempts:",Turns)


        elif 'dollar to indian rupees' in query:
            dollartoinr()

        elif 'indian rupees to dollar' in query:
            inrtodollar()

        elif 'calculate' in query:
            r = sr.Recognizer()
            my_mic_device = sr.Microphone(device_index=1)
            with my_mic_device as source:
                speak("Say what you want to calculate, example 3 plus 3")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print("You said")
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    'Mod' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]

            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("Your result is")
            speak(eval_binary_expr(*(my_string.split())))

        # if 'what is' or 'who is' in query:
        #     query= query.replace("wikipedia","") 
        #     results=wikipedia.summary(query, sentences=3)
        #     speak("According to wikipedia")
        #     speak(results) 

        elif 'saying of techno india siliguri' in query:
            speak("Knowledge is power")

        elif 'who developed you' in query:
            speak(" Hey, I was  developed by a  group  of  students   in   Techno   India   Siliguri,  atl  lab  who  brought  me  to  life")

        elif 'how many teachers are there in techno india siliguri' in query:
            speak("100 teachers are there in techno india siliguri")

        elif "tell me about a cartoon character" in query:
            speak("Which one?")
            cartoon=takeCommand()
            cartoon= cartoon.replace("wikipedia","") 
            results=wikipedia.summary(cartoon, sentences=3)
            speak(results)
