#Adapation of
from gtts import gTTS
import speech_recognition as sr
import cython
import os
import re
import webbrowser
import smtplib
import requests
import wolframalpha
import wikipedia
import datetime
import random
import cv2
import face_recognition
from selenium import webdriver
from time import sleep
client = wolframalpha.Client('<Client ID>')
i = 0
def talkToMe(audio):
    "speaks audio passed as argument"
    print("Adam: " + audio)
    for line in audio.splitlines():
        os.system("say " + audio)
        text_to_speech = gTTS(text=audio, lang='en-us')
        text_to_speech.save('audio.mp3')
        os.system('mpg123 audio.mp3')
def takePhoto():
    for i in range(11):
        ret, frame = video_capture.read()
        cv2.imwrite('<path to save photo>', frame)
def show_box():
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    print("all windows closed")
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-us')
        print('Master ?: ' + query + '\n')
    except sr.UnknownValueError:
        talkToMe('Sorry Master <NAME>  I did not get that! Try typing the command in this time!')
        query = str(input('Command: '))
    return query
def insta_cross_refrence_folowers_with_following():
    from selenium import webdriver
    from time import sleep
    following_list = []
    followers_list = []
    handle = input()
    driver = webdriver.Chrome('<path to chrome driver on computer>') #this will save the instance of that chrome drive practically saving the data
    username = "<Account Username>"
    password = "<Password>"
    driver.get(f"https://www.instagram.com/{handle}/")
    talkToMe("opening instagram")
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    sleep(1)
    talkToMe("Login to my account successful")
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(1)
    count_following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
    print(count_following.text)
    talkToMe("Following count is " + str(count_following) + "sir")
    driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
    sleep(4)
    print(driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a').text)
    print("..............................")
    print("FOLLOWING")
    print("..............................")
    talkToMe("Checking following")
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div")
    last_ht, ht = 0, 1
    for i in range(int(count_following.text) - 1):
        if i == 16:
            sleep(2)
        if i == 32:
            sleep(2)
        if i == 61:
            sleep(2)
        if i == 70:
            while last_ht != ht:
                last_ht = ht
                sleep(1)
                ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight
            """, scroll_box)
        if i == 119:
            sleep(2)
        if i == 280:
            sleep(2)
        if i == 340:
            sleep(2)
        if i == 500:
            sleep(2)
        if i == 630:
            sleep(2)
        if i == 710:
            sleep(2)
        if i == 820:
            sleep(2)
        following = driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{i+1}]/div/div[1]/div[2]/div[1]/a")
        print(following.text)
        following_list.append(following.text)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
    sleep(1)
    count_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    sleep(2)
    driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
    sleep(2)
    scroll_box2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    print("..............................")
    print(count_followers.text)
    talkToMe("following count is " + str(count_followers) + " sir")
    print("FOLLOWERS")
    talkToMe("checking followers")
    print("..............................")
    for j in range(int(count_followers.text) - 1):
        if j == 16:
            sleep(2)
        if j == 32:
            sleep(2)
        if j == 61:
            sleep(2)
        if j == 70:
            while last_ht != ht:
                last_ht = ht
                sleep(1)
                ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight
            """, scroll_box2)
        if j == 119:
              sleep(2)
        f = driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{j+1}]/div/div[1]/div[2]/div[1]/a")
        print(f.text)
        followers_list.append(f.text)
        if j == 280:
            sleep(2)
        if j == 340:
            sleep(2)
        if j == 500:
            sleep(2)
        if j == 630:
            sleep(2)
        if j == 710:
            sleep(2)
        if j == 820:
            sleep(2)
    talkToMe("cross refrencing followers to following")
    scum_bags = list(set(following_list) - set(followers_list))
    if scum_bags == []:
        print("everyone u follow followers back")
        talkToMe("everyone seems to be following you back sir")
    else:
        print("some people")
        talkToMe("found people sir you might want to have a look")
    print(scum_bags)
    print(len(scum_bags))
    talkToMe("check complete Mr/Ms ?")
def assistant(query):
    "if statements for executing commands"
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        m = "morning"

    if currentH >= 12 and currentH < 18:
        m = "afternoon"

    if currentH >= 18 and currentH !=0:
        m = "evening"

    if "hello" in query:
        name = ""
        talkToMe("Hello Master ? " +  name + " its always good to see you again on this fine " + m)
    if "insatgram check":
        talkToMe("Enter handle please sir  or friend")
        insta_cross_refrence_folowers_with_following()
    elif "open my website" in query:
        talkToMe("opening your website and my I say sir it is a good looking one")
        webbrowser.open('http://www.jasonkmoses.ga/index.php')

    elif "watch the laptop" in query:
        while True:
            talkToMe("Watch protocol on This computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me This computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get nearThis computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near  This computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near  This computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near  This computer is begin monitiored if you are to take it the user will imdetially get a notification of your wareabouts please do not take the computer and please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near me please do not get near  ")

    elif "open emails" in query:
        talkToMe("opening your emails")
        webbrowser.open('https://www.gmail.com/')

    elif "open Youtube" in query:
        talkToMe("opening youtube up enjoy cat videos sir")
        webbrowser.open("https://www.youtube.com/")

    elif "play music" in query:
        talkToMe("opening music my favourite song is.. let me just sing it sir: the synergy illuminates unites man and machine heartbeat hardware standing tall. together we complete like titans we through fire man and machine mmmm sorry sir playing music now.")
        music_folder = "<music path/>"
        music = ["<music file name>"]
        random_music = music_folder + random.choice(music) + '.mp4'
        os.system(random_music)

    elif "play your favourite song" in query or "what is your favourite song" in query:
        webbrowser.open("https://www.youtube.com/watch?v=ZJQlGNjJJ5A&ab_channel=TryHardNinja")
        talkToMe("I love this song ❤️ Together we complete")

    elif "open Facebook" in query:
        talkToMe("opening your Facebook account")
        webbrowser.open("https://www.facebook.com/")

    elif "open Instagram" in query:
        webbrowser.open("https://www.instagram.com/")
        talkToMe("opened Instagram")

    elif "perfect" in query or "perfect Jarvis" in query or "perfect jarvis"  in query or "good" in query or "fine" in query or "great" in query:
        talkToMe("Thank you sir I am here to serve!")


    elif "bad" in query or "bad Jarvis" in query or "bad jarvis" in query or "bad" in query or "not good" in query or "not nice" in query:
        talkToMe("I have been humilated I will take notes sir")


    elif "play some French songs" in query:
        talkToMe("playing a french song for your french lessons")
        french_songs = ["https://www.youtube.com/watch?v=vtNJMAyeP0s&ab_channel=IndilaVEVO","https://www.youtube.com/watch?v=m65jhGwtWrg&ab_channel=IndilaVEVO","https://www.youtube.com/watch?v=K5KAc5CoCuk&ab_channel=IndilaVEVO"]
        webbrowser.open(random.choice(french_songs))

    elif "play my favourite song" in query:
        talkToMe("trick question sir you dont have just one song you have many favourite songs sir I remember let me choose randomley")
        favSongs = ["<list of fav songs u have on youtube>"]
        webbrowser.open_new_tab(random.choice(favSongs))

    elif "call" in query:
        talkToMe("calling ?")
        webbrowser.open("enter url")


    elif "what is your favourite food" in query:
        talkToMe("bytes 1011110")


    elif "what is your favourite device" in query:
        talkToMe("iPhone X")


    elif "how are you" in query or "how are you Jarvis" in query:
        talkToMe("I am fine sir and you?")


    elif "what are you" in query:
        talkToMe("I am a lower level of a AI using random choices to determine an outcome for now")

    elif "greet" in query:
        name = "and friend"
        talkToMe("Hello person who knows Mr/Ms can I help you with anything?")
        if "Yes" in query:
            talkToMe("Very well name the request")
        elif "No" in query:
            talkToMe("Very well")
            flag = o
    elif "greet my mother" in query:
        talkToMe("Hello Master Jasons mother hope you are enjoying your " + m + " he must get the looks from you")

    elif "greet my father" in query:
        talkToMe("Hello Master Randolph you have such a smart child he must get it from you")

    elif "greet my brother" in query:
        talkToMe("which one?")

    elif "greet my granny" in query:
        talkToMe("Hello Master Ruby it is good to see you are great you must share your wisdom sometime")

    elif "that will be all" in query:
        name = ""
        talkToMe("very well enjoy your day master Jason ")
        flag = o
    elif "bye" in query or "goodbye" in query:
        name = ""
        talkToMe("Alrigth then goodbye Master Jason I will take my leave.")
        flag = o
    else:
        query = query
        talkToMe('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                talkToMe('WOLFRAM-ALPHA says this about - ')
                talkToMe('I got it sir.')
                talkToMe(results)
            except:
                results = wikipedia.summary(query, sentences=2)
                talkToMe('Got it.')
                talkToMe('WIKIPEDIA says - ')
                talkToMe(results)
        except:
            webbrowser.open('www.google.com')
talkToMe("Checking if it is master ?")
talkToMe('Hello sir')
assistant(myCommand())
