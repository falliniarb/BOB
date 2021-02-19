
import winshell
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from random import randint
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import random 
import tkinter
from tkinter import *
from functools import partial 
from tkinter import messagebox 
from copy import deepcopy 

sign = 0
global board 
board = [[" " for x in range(3)] for y in range(3)] 


def winner(b, l): 
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l)) 


def get_text(i, j, gb, l1, l2): 
	global sign 
	if board[i][j] == ' ': 
		if sign % 2 == 0: 
			l1.config(state=DISABLED) 
			l2.config(state=ACTIVE) 
			board[i][j] = "X"
		else: 
			l2.config(state=DISABLED) 
			l1.config(state=ACTIVE) 
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j]) 
	if winner(board, "X"): 
		gb.destroy() 
		box = messagebox.showinfo("Winner", "Player 1 won the match") 
	elif winner(board, "O"): 
		gb.destroy() 
		box = messagebox.showinfo("Winner", "Player 2 won the match") 
	elif(isfull()): 
		gb.destroy() 
		box = messagebox.showinfo("Tie Game", "Tie Game") 


def isfree(i, j): 
	return board[i][j] == " "


def isfull(): 
	flag = True
	for i in board: 
		if(i.count(' ') > 0): 
			flag = False
	return flag 


def gameboard_pl(game_board, l1, l2): 
	global button 
	button = [] 
	for i in range(3): 
		m = 3+i 
		button.append(i) 
		button[i] = [] 
		for j in range(3): 
			n = j 
			button[i].append(j) 
			get_t = partial(get_text, i, j, game_board, l1, l2) 
			button[i][j] = Button( 
				game_board, bd=5, command=get_t, height=4, width=8) 
			button[i][j].grid(row=m, column=n) 
	game_board.mainloop() 


def pc(): 
	possiblemove = [] 
	for i in range(len(board)): 
		for j in range(len(board[i])): 
			if board[i][j] == ' ': 
				possiblemove.append([i, j]) 
	move = [] 
	if possiblemove == []: 
		return
	else: 
		for let in ['O', 'X']: 
			for i in possiblemove: 
				boardcopy = deepcopy(board) 
				boardcopy[i[0]][i[1]] = let 
				if winner(boardcopy, let): 
					return i 
		corner = [] 
		for i in possiblemove: 
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]: 
				corner.append(i) 
		if len(corner) > 0: 
			move = random.randint(0, len(corner)-1) 
			return corner[move] 
		edge = [] 
		for i in possiblemove: 
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]: 
				edge.append(i) 
		if len(edge) > 0: 
			move = random.randint(0, len(edge)-1) 
			return edge[move] 


def get_text_pc(i, j, gb, l1, l2): 
	global sign 
	if board[i][j] == ' ': 
		if sign % 2 == 0: 
			l1.config(state=DISABLED) 
			l2.config(state=ACTIVE) 
			board[i][j] = "X"
		else: 
			button[i][j].config(state=ACTIVE) 
			l2.config(state=DISABLED) 
			l1.config(state=ACTIVE) 
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j]) 
	x = True
	if winner(board, "X"): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Winner", "Player won the match") 
	elif winner(board, "O"): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Winner", "Computer won the match") 
	elif(isfull()): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Tie Game", "Tie Game") 
	if(x): 
		if sign % 2 != 0: 
			move = pc() 
			button[move[0]][move[1]].config(state=DISABLED) 
			get_text_pc(move[0], move[1], gb, l1, l2) 


def gameboard_pc(game_board, l1, l2): 
	global button 
	button = [] 
	for i in range(3): 
		m = 3+i 
		button.append(i) 
		button[i] = [] 
		for j in range(3): 
			n = j 
			button[i].append(j) 
			get_t = partial(get_text_pc, i, j, game_board, l1, l2) 
			button[i][j] = Button( 
				game_board, bd=5, command=get_t, height=4, width=8) 
			button[i][j].grid(row=m, column=n) 
	game_board.mainloop() 


def withpc(game_board): 
	game_board.destroy() 
	game_board = Tk() 
	game_board.title("Tic Tac Toe") 
	l1 = Button(game_board, text="Player : X", width=10) 
	l1.grid(row=1, column=1) 
	l2 = Button(game_board, text = "Computer : O", 
				width = 10, state = DISABLED) 
	
	l2.grid(row = 2, column = 1) 
	gameboard_pc(game_board, l1, l2) 

 
def withplayer(game_board): 
	game_board.destroy() 
	game_board = Tk() 
	game_board.title("Tic Tac Toe") 
	l1 = Button(game_board, text = "Player 1 : X", width = 10) 
	
	l1.grid(row = 1, column = 1) 
	l2 = Button(game_board, text = "Player 2 : O", 
				width = 10, state = DISABLED) 
	
	l2.grid(row = 2, column = 1) 
	gameboard_pl(game_board, l1, l2) 


def play(): 
	menu = Tk() 
	menu.geometry("250x250") 
	menu.title("Tic Tac Toe") 
	wpc = partial(withpc, menu) 
	wpl = partial(withplayer, menu) 
	
	head = Button(menu, text = "---Welcome to tic-tac-toe---", 
				activeforeground = 'red', 
				activebackground = "yellow", bg = "red", 
				fg = "yellow", width = 500, font = 'summer', bd = 5) 
	
	B1 = Button(menu, text = "Single Player", command = wpc, 
				activeforeground = 'red', 
				activebackground = "yellow", bg = "red", 
				fg = "yellow", width = 500, font = 'summer', bd = 5) 
	
	B2 = Button(menu, text = "Multi Player", command = wpl, activeforeground = 'red', 
				activebackground = "yellow", bg = "red", fg = "yellow", 
				width = 500, font = 'summer', bd = 5) 
	
	B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red', 
				activebackground = "yellow", bg = "red", fg = "yellow", 
				width = 500, font = 'summer', bd = 5) 
	head.pack(side = 'top') 
	B1.pack(side = 'top') 
	B2.pack(side = 'top') 
	B3.pack(side = 'top') 
	menu.mainloop() 








engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go on I'm Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:   
        print("Say that again please...")  
        return "None"
    return query





def wishMe():

    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        Greet = 'Hello and Good Morning Sir,'

    elif (hour>=12 and hour<18):
        Greet = 'Hello and Good Afternoon Sir,'   

    else:
        Greet = 'Hello and Good Evening Sir,'  


    speak(f"{Greet} I am Bob, your Virtual desktop assistant.")       
    

        

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

  
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        



        elif ('introduce yourself' in query):
            speak('I am Bob, version 1 point O , your personal Virtual Desktop Assistant. I am developed using python 3 and I can perform certain tasks to reduce your work load.')



        elif ('open youtube' in query):
            webbrowser.open("youtube.com")
            speak("youtube is open now")

        elif ('open google' in query):
            webbrowser.open("google.com")
            speak("google is open now")

        elif ('open stack overflow' in query):
            webbrowser.open("stackoverflow.com") 
            speak("stackoverflow is open now")

        elif ('open facebook' in query):
            webbrowser.open("www.facebook.com") 
            speak("facebook is open now")       

        elif ('open flipkart' in query):
            webbrowser.open("www.flipkart.com")
            speak("flipkart is open now")

        elif ('open amazon' in query):
            webbrowser.open("www.amazo898ion.com")
            speak("amazon is open now")

        elif ('open medium' in query):
            webbrowser.open("www.medium.com")
            speak("medium is open now")
        
        elif ('open codezinger' in query):
            webbrowser.open("codezinger.com")
            speak("codezinger is open now")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")


        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(f"Answer to {question} is {answer}")
            print(answer)
        

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        
        elif ('play music' in query):
            music_dir = 'C:\\Users\\Aaditya Verma\\Music\\iTunes\\iTunes Media\\Music\\AC_DC\\Iron Man 2'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[randint(0,len(songs) - 1 )]))

        elif ('the time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif ('open outlook' in query):
            outlook_Path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(outlook_Path)

        elif ('open msteams' in query):
            teams_path = "C:\\Users\\Aaditya Verma\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
            os.startfile(teams_path)

        elif ('open pycharm' in query):
            charm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(charm_path)
        
        elif ('tic tac toe' in query):  
            play()      
             
        elif "goodbye" in query or "ok bye" in query or "stop" in query:
            print('Alright, have a good day Sir!')
            speak('Alright, have a good day Sir!')
            break

        elif "log off" in query or "sign out" in query:
            speak("Alright Sir, your pc will log off in 10 seconds. Make sure you exit from all of the applications")
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])

        elif 'shutdown system' in query:
                speak("You have 10 seconds to close all the applications.")
                time.sleep(10)
                speak("Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
