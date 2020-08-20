#importing modules/libraries
import pyttsx3       # convert text to speech
import datetime      # get date and time
import wikipedia     # wikipedia search
import webbrowser as wb  #search on chrome
import os                #system settings 
import pyautogui         #screenshot
import pyjokes           #python programming jokes
import oneliners         #common one liners
import psutil            #cpu stats

#initiallising text to speech
genie=pyttsx3.init()

def speak(audio):
    genie.say(audio)
    genie.runAndWait()

#real-time date and time functions 
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    Date=datetime.datetime.now().date()
    print(Date)
    speak(Date)

#smart greeting function which greets according to current time(morning,afternoon and evening)
def greet():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Good Morning!,Welcome Back Master!")
        speak("Good Morning!,Welcome Back Master!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!,Welcome Back Master!")
        speak("Good Afternoon!,Welcome Back Master!")
    elif hour>=18 and hour<24:
        print("Good Evening!,Welcome Back Master!")
        speak("Good Evening!,Welcome Back Master!")   
    print("Can i help you with anything?")      
    speak("Can i help you with anything?")

#input command function
def takecommand():
    query=input("Genie,My Wish is:")
    return query

#screenshot function
def screenshot():
    img=pyautogui.screenshot()
    img.save("C:/Users/Tushar Jain/Desktop/ss.png")

#cpu and battery stat function
def cpu():
    per=str(psutil.cpu_percent())
    print("the cpu is at" +per+"percent")
    speak("the cpu is at" +per+"percent")
    bat=str(psutil.sensors_battery())
    print(bat)
    speak(bat)

#common one-liner and python joke function
def joke1():
    speak(oneliners.get_random())

def joke2():
    speak(pyjokes.get_joke())

#main function
if __name__ == "__main__" :
 print("""          Hiii Thankyou for rubbing the magic lamp! I am the genie of this lamp!
          Unlike providing you with a limited number of 3 wishes, i can help you
          with anything! But because of the ongoing pandemic my powers are limited to 
          the following: 
          1.date 2.time 3.wikipedia_search 4.launch_website_on_chrome 5.logout_restart_shutdown_system
          6.Taking_notes_and_remind 7.Screenshot 8.CPU_Stats 9.Playlist 10.Jokes""")
 speak("""Hi! Thankyou for rubbing the magic lamp! I am the genie of this lamp!
        Unlike providing you with a limited number of 3 wishes, i can help you
        with anything! But because of the ongoing pandemic my powers are limited to 
        the following:""")      
 x=input("do you wish to continue(y/n)?")
 if x=='y':
    greet()
    while True:
        query=takecommand()
        if "date" in query:      #gets u the current date
            date()
        
        elif "time" in query:    #gets u the current time 
            time()
        
        elif "wikipedia" in query:       #provides a short summary of the wikipedia page of the topic searched
            print("which article should i search?")
            speak("which article should i search?")
            search=input("please provide me with the name: ")
            result=wikipedia.summary(search,sentences=2)
            print(result)
            speak(result)
        
        elif "chrome" in query:                  #open any site on chrome
            print("what should i search?")
            speak("what should i search?")
            search=str(input("enter:"))
            chromepath ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'   
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif "logout" in query:                      #forcefully logs out of the system
            os.system("shutdown -1")
        
        elif "shutdown" in query:                    #forcefully shutsdown the system
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:                     #forcefully restarts the system
            os.system("shutdown /r /t 1")

        elif "note" in query:                        #Creates a notepad file on the desktop named data and takes note. 
            print("what should I note?")             #If already present, it appends the file with new data
            speak("what should I note?")
            data=input("note:")
            print("I will be noting "+data)
            speak("I will be noting "+data)
            note=open('C:/Users/Tushar Jain/Desktop/data.txt','w')
            note.write(data)
            note.close()
        
        elif "remind" in query:                                          #reads out the content of file data.txt
            note=open('C:/Users/Tushar Jain/Desktop/data.txt','r')
            print("you told me to note " +note.read()) 
            speak("you told me to note "+note.read())     

        elif "capture" in query:                                    #takes a screenshot of the screen
            screenshot()
            speak("Successfully captured")

        elif "cpu" in query:                         #provides cpu usage and battery stat
            cpu()

        elif "playlist" in query:
            sdir="C:/Users/Tushar Jain/Desktop/Music/"                #plays local playlist in music folder
            slist=os.listdir(sdir)
            os.startfile(os.path.join(sdir,slist[0]))  

        elif "joke" in query:
            print("which type of joke, programming or normal?")
            speak("which type of joke, programming or normal?")           #joke function
            type=input("choice: ")
            if type=="programming":
                joke2()
                while True:
                    print("do you want more?")
                    speak("do you want more?")
                    option=input("yes or no: ")
                    if option=="yes":
                        joke2()
                    elif option=="no":
                        break

            else:
                joke1()
                while True:
                    print("do you want more?")
                    speak("do you want more?")
                    option=input("yes or no: ")
                    if option=="yes":
                        joke1()
                    elif option=="no":
                        break

        elif "offline" in query:                      #exit
            quit()

