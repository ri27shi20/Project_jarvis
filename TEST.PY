from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import wikipedia
import webbrowser
import datetime
import pywhatkit as pwt
from selenium import webdriver
# FOR CONTROLING WEBSITE
# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import multiprocessing
import asyncio
import base64 
import json
import pyaudio
import websockets   
 

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
anime=voices[0]
engine.setProperty('voice',anime.id)
""" LST=speak("speak again") """
# engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("hello Good morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        speak(' what can i do for you ')
    else:
        # speak("Good night Sir")
        speak('Sir  what can i do for you ')
        # LST=speak("speak again")
class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            
            audio = R.listen(source, 0, 7)
            
        try:
            text = R.recognize_google(audio,language='en-in')
            print("Recog......")    

            print("YOU ",text)
        except Exception:
            
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'goodbye' in self.query:
                speak("I'M leaving, sir!")
                sys.exit()
            # elif 'open google' in self.query:
            #     webbrowser.open('www.google.co.in')
            #     speak("opening google")
            # elif 'open youtube' in self.query:
            #     webbrowser.open("www.youtube.com")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            elif 'youtube' in self.query:
                speak("Opening youtube")
                # webbrowser.open("youtube.com")
                ytsrch = self.query.replace("youtube", "")
                pwt.playonyt(ytsrch)
            elif 'favourite songs' in self.query:
                speak("Sure sir")
                # webbrowser.open("youtube.com")
                ytsrch = self.query.replace("youtube", "")
                pwt.playonyt("dendlions")
            elif 'favourite song' in self.query:
                speak("Sure sir")
                # webbrowser.open("youtube.com")
                ytsrch = self.query.replace("youtube", "")
                pwt.playonyt("dendlions")

            elif 'repeat' in self.query:
                # webbrowser.open("youtube.com")
                a = self.query.replace("repeat", "")
                speak(a)
            elif 'sab ko bolo' in self.query:
                # webbrowser.open("youtube.com")
                a = self.query.replace("sab ko bolo", "")
                speak(a)
            elif 'hello' in self.query:
                # webbrowser.open("youtube.com")
                speak("hello sir ")
            
            elif 'who are you' in self.query:
                # webbrowser.open("youtube.com")
                speak("Iam your personal voice assistance")
            
            elif 'how are you' in self.query:
                # webbrowser.open("youtube.com")
                speak("as always ready for you sir ")
                speak("what about you")
            elif 'what can you do' in self.query:
                # webbrowser.open("youtube.com")
                speak("sir i can play songs on youtube ")
                speak("open whatsapp ")
                speak("perform google searches ")
                speak("perform wikipedia searches ")

            elif ('exit') in self.query:
                speak('yes sir, have a nice day')
                press_and_release('windows + d')
                sys.exit()
                break 
            # webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("Opening Google")
                webbrowser.open("google.com")
            elif 'stop' in self.query:
                 LST=("speak again")          
               

            elif 'karen' in self.query:
                anime=voices[1]
                engine.setProperty('voice',anime.id)
                speak("i am listening sir")
                anime=voices[0]
                engine.setProperty('voice',anime.id)

            elif 'open stack overflow' in self.query:
                speak("Opening stack overflow")
                webbrowser.open("stackoverflow.com")

            elif 'open web whatsapp' in self.query:
                speak("Opening whatsapp")
                webbrowser.open("web.whatsapp.com")
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            # elif 'open whatsapp' in self.query:
            #     codePath = "C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            #     speak("Opening whatsapp")
            #     os.startfile(codePath)
            # elif 'close whatsapp' in self.query:
            #     codePath = "C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            #     speak("closing whatsapp")
            #     os.system("taskkill /f /im WhatsApp.exe")
            elif 'sanket mhatre' in self.query:
                codePath1= "D:\Downloads\Deadpool 2 is BACK with Original Dubbing _.mp4"
                speak("ok")
                os.startfile(codePath1)
            elif 'video' in self.query:
                codePath2 = "D:\\songs_jarvic\\videoplayback.mp4"
                speak("Yes Sir")
                os.startfile(codePath2)
            elif 'shutdown' in self.query:
                speak("Sure Sir, have a nice day")
                # os.system("shutdown /s /t 2")
            elif 'shut down' in self.query:
                speak("Sure Sir, have a nice day")
                # os.system("shutdown /s /t 2")
            elif 'close it' in self.query:
                press_and_release('ctrl + w')
                speak("done sir")
            elif 'close' in self.query:
                press_and_release('ctrl + w')
                speak("done sir")
            elif 'fast forward' in self.query:
                press_and_release('shift + period')
            elif 'slow down' in self.query:
                press_and_release('shift + comma')
            elif 'switch' in self.query:
                press_and_release('alt + tab')
            elif 'close all' in self.query:
                os.startfile("D:\\one drive\\OneDrive\\Desktop\\jarvic\\JV.BAT")
                press_and_release('alt + tab')
                time.sleep(0.55)
                press_and_release('ctrl + s')
                press_and_release('alt + f4')
                time.sleep(0.35)
                press_and_release('alt + tab')  
                time.sleep(0.55)
                press_and_release('ctrl + s')
                press_and_release('alt + f4')
                time.sleep(0.35)
                press_and_release('alt + tab')
                time.sleep(0.55)
                press_and_release('ctrl + s')
                press_and_release('alt + f4')
                time.sleep(0.35)
                press_and_release('alt + tab')
                time.sleep(0.55)
                press_and_release('ctrl + s')
                press_and_release('alt + f4')
                time.sleep(0.35)
                press_and_release('alt + tab')
                time.sleep(0.55)
                press_and_release('ctrl + s')
                press_and_release('alt + f4')
                time.sleep(0.35)
            elif 'search' in self.query:
                import wikipedia as googleScrap
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("jariv", "")
                self.query = self.query.replace("google", "")
                speak('this is what i found')
                pwt.search(self.query)
                try:
                    result = googleScrap.summary(self.query,3)
                    speak(result)
                except:
                    speak("No readable data ")
            elif '.com' in self.query:
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("jarvic", "")
                self.query = self.query.replace("on google", "")
                self.query = self.query.replace("open", "")
                self.query = self.query.replace(" ", "")
                speak("sure sir")
                webbrowser.open_new("https://"+self.query)
            else:
                from ChatBot.ChatBot import ChatterBot
                reply = ChatterBot(self.query)
                speak(reply)
                if 'bye' in self.query:
                    break
                elif 'goodbye' in self.query:
                    sys.exit()

            # elif 'play music' in query:
            #     music_dir = 'D:\\songs_jarcvis'
            #     songs = os.listdir(music_dir)
            #     print(songs)
            #     os.startfile(os.path.join(music_dir, songs[0]))

            # elif 'the time' in query:
            #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #     speak(f"Sir, the time is {strTime}")

            # elif 'open whatsapp' in query:
            #     codePath = "C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            #     speak("Opening whatsapp")
            #     os.startfile(codePath)

            # elif 'close whatsapp' in query:
            #     codePath = "C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            #     speak("closing whatsapp")
            #     os.system("taskkill /f /im WhatsApp.exe")

            # elif 'sanket mhatre' in query:
            #     codePath1 = "D:\Downloads\Deadpool 2 is BACK with Original Dubbing _.mp4"
            #     speak("ok")
            #     os.startfile(codePath1)

            # elif 'video' in query:
            #     codePath2 = "D:\\songs_jarvic\\videoplayback.mp4"
            #     speak("Yes Sir")
            #     os.startfile(codePath2)
            # elif 'shutdown' in query:

            #     speak("ok Sir")
            #     os.system("shutdown /s /t 3")
            # elif 'close it' in query:

            #     press_and_release('ctrl + w')
            # elif 'close all' in query:
            #     os.startfile("D:\\one drive\\OneDrive\\Desktop\\jarvic\\JV.BAT")
            #     press_and_release('alt + tab')
            #     time.sleep(0.55)
            #     press_and_release('ctrl + s')
            #     press_and_release('alt + f4')
            #     time.sleep(0.35)
            #     press_and_release('alt + tab')  
            #     time.sleep(0.55)
            #     press_and_release('ctrl + s')
            #     press_and_release('alt + f4')
            #     time.sleep(0.35)
            #     press_and_release('alt + tab')
            #     time.sleep(0.55)
            #     press_and_release('ctrl + s')
            #     press_and_release('alt + f4')
            #     time.sleep(0.35)
            #     press_and_release('alt + tab')
            #     time.sleep(0.55)
            #     press_and_release('ctrl + s')
            #     press_and_release('alt + f4')
            #     time.sleep(0.35)
            #     press_and_release('alt + tab')
            #     time.sleep(0.55)
            #     press_and_release('ctrl + s')
            #     press_and_release('alt + f4')
            #     time.sleep(0.35)

            # elif 'search' in query:
            #     import wikipedia as googleScrap
            #     query = query.replace("search", "")
            #     query = query.replace("jariv", "")
            #     query = query.replace("google", "")
            #     speak('this is what i found')
            #     pwt.search(query)

            #     try:
            #         result = googleScrap.summary(query,3)
            #         speak(result)
            #     except:
            #         speak("No readable data ")
            # elif '.com' in query:
            #     query = query.replace("search", "")
            #     query = query.replace("jarvic", "")
            #     query = query.replace("on google", "")
            #     query = query.replace("open", "")
            #     query = query.replace(" ", "")
            #     webbrowser.open_new("https://"+query)











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(D:/one drive/OneDrive/Desktop/jv/jv1/new latest/GUI-Jarvis-main/GUI-Jarvis-main/lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("D:/one drive/OneDrive/Desktop/jv/jv1/new latest/GUI-Jarvis-main/GUI-Jarvis-main/lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("D:/one drive/OneDrive/Desktop/jv/jv1/new latest/GUI-Jarvis-main/GUI-Jarvis-main/lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())