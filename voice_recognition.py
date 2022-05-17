# Import necessary functionality
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from selenium import webdriver  # webdriver is used to interact with the browser
from selenium.webdriver.common.keys import Keys  # Keys are the physical key commands on the keyboard
from selenium.webdriver.support.ui import Select  # This imports a module that helps select actual items on the page
from selenium.webdriver import ActionChains
import os


### Set up the assistant
# instantiate a recognizer that listens to audio
listener = sr.Recognizer()
# initialize an engine that allows computer to speak to you
engine = pyttsx3.init()
# select specific voice (Male or Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# define function that allows AI to talk to you
def talk(text):
    engine.say(text)
    engine.runAndWait()

# define function that governs the listening of commands
def take_command():
    # possible uncontrollable issues may occur (account for that)
    try:
        with sr.Microphone() as source: # create a microphone called source
            print('I am listening ...') # print a message to give speaker their que
            voice = listener.listen(source) # have the recognizer object listen to the source (audio from the microphone)
            command = listener.recognize_google(voice) # have the recognizer recognize audio by associating with google audio files
            command = command.lower() # lower case the command
            #print(command)  # print out what was heard by the computer
    except:
        pass
    return command

### *********************************** Features of DON ***********************************************************###
# DON plays a YT video
def play_content(command):
    content = command.replace('play', '')
    talk('playing ' + content) # what Don would say
    print('Playing ' + content) # confirmation to user
    pywhatkit.playonyt(content) # search up the content on youtube

# DON gives current time
def time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current time: '+ time)
    talk('The current time is ' + time)

# DON searches up a specific website
def website_search(command):
    # Construct driver (for web searching functionality)
    PATH = r"C:\Users\DonyeWakefield\Desktop\Coding\drivers\chromedriver.exe"  # Find out where our chromedriver is located (We do this after we installed it)
    driver = webdriver.Chrome(
        PATH)  # webdriver object and use Chrome method, which contains an argument PATH. Therefore I create
    # create action object (performing clicks)
    action = ActionChains(driver)

    driver.implicitly_wait(120)  # tell the driver to wait for 2 minutes before closing the interactive connection with the browser
    # specify the specific website from the command
    website = command.replace('go to', '')
    if 'amazon' in website:
        website = "https://www.amazon.com/gp/yourstore?ie=UTF8&ref=ox_checkout_redirects_yourstore"
    talk("going to amazon")
    driver.get(website)  # use access member function get(string) on driver and this will allow us to access the website

    # What does the user want to search for on the website?
    talk("What would you like to search for on Amazon?")
    search = take_command()

    # accessing the website and searching within it
    talk("Just a second")
    elem = driver.find_element_by_id("twotabsearchtextbox")  # We found the input field
    elem.clear()  # clear out the input field
    elem.send_keys(search)  # enter these keys
    elem.send_keys(Keys.RETURN)  # Then hit enter to do the search
    talk("is there anything else i can do for you?")

# DON does basic math
def basic_math():
    talk("give me the numbers, and i will do the calculation for you")
    statement = take_command() # numbers given as a string
    numbers = statement.split()  # split the string

    if '+' in statement:
        ### Addition
        list1 = []
        for i in numbers:
            if i != '+':
                i = int(i)
                list1.append(i)
        print(f"{list1[0]} + {list1[1]} = {list1[0] + list1[1]}")  # showcase the math statement
        talk(f"{list1[0]} + {list1[1]} is {list1[0] + list1[1]}")  # DON says it

    if '-' in statement:
        ### Subtraction
        list1 = []
        for i in numbers:
            if i != '-':
                i = int(i)
                list1.append(i)
        print(f"{list1[0]} - {list1[1]} = {list1[0] - list1[1]}")  # showcase the math statement
        talk(f"{list1[0]} - {list1[1]} is {list1[0] - list1[1]}")  # DON says it

    if '*' in statement:
        ### Multiplication
        list1 = []
        for i in numbers:
            if i != '*':
                i = int(i)
                list1.append(i)
        print(f"{list1[0]} * {list1[1]} = {list1[0] * list1[1]}")  # showcase the math statement
        talk(f"{list1[0]} times {list1[1]} is {list1[0] * list1[1]}")  # DON says it

    if '/' in statement:
        ### Division
        list1 = []
        for i in numbers:
            if i != '/':
                i = int(i)
                list1.append(i)
        print(f"{list1[0]} / {list1[1]} = {list1[0] / list1[1]}")  # showcase the math statement
        talk(f"{list1[0]} divided by {list1[1]} is {list1[0] / list1[1]}")  # DON says it


### *************************************** DON Running ************************************************************###
### Start-up speech
engine.say("Why Hello. I am Don, your personal AI assistant.")
           #"I am programmed to answer and perform virtually any and all questions or commands"
           #"that you wish to ask. Whether it be jokes, the time, weather, videos, music, or more, I will "
           #"try and assist you. Just call DON when you want to ask or command something.")
engine.say("How can I help you?")
engine.runAndWait()
### taking command
cmd = take_command()

###***************************************** Calling Features *****************************************************###
### User wants to play a youtube video
if 'play' in cmd:
    play_content(cmd)

### User wants the current time
if 'time' in cmd:
    time()

### User wants to shop at a particular website
if 'go to' in cmd:
    website_search(cmd)

### User wants to do basic math
if 'math' in cmd:
    basic_math()

### User wants to know the weather







### User wants to hear a funny joke

### User wants to hear a story (user picks the genre of story (i.e. horror, funny, etc.)

### User wants to search up anything on google


###*********** interact with the OS ***********###
### User wants to create a word document

### User wants to open up a file on their computer

### User wants to create a directory on their computer


###*********** Shutdown Something ***********###
### User wants to shutdown their computer

### User wants to restart their computer

### User wants to close down the DON AI assistant






###************************************* Backburner functionality ****************************************************###

   # if 'loop' in command2:
        # loop the video
        #video_elem = driver.find_element_by_class_name("video-stream html5-main-video")
        #action.context_click(video_elem)  # right click the video
        #elem = driver.find_element_by_class_name("ytp-menuitem-label")  # find the loop button
        #action.context_click(elem).perform()  # click on the loop button
