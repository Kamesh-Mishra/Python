# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:46:43 2020

@author: Kamesh
"""


# how to find mobile number is valid or not 
"""
three main conditions to check your number is  valid or not (according to india)

1 all numbers is begin with 0 and 91
2 middle order contains 7 or 8 or 9 digits
3 then contain 9 number of digits

"""



import re

def number(n):
    condition = re.compile("(0/91)?[7-9][0-9]{9}")
    return condition.match(n)

n = input("enter your mobile number : ")

if (number(n)):
    print("valid number")
else:
    print("invalid number") 
    

    
    
    
    
    
############################################


# making a graph using any data 


import matplotlib.pyplot as plt

xaxis  = [1,2,3,4,5] 
yaxis  = [1,4,9,16,25]

plt.bar(xaxis, yaxis)
plt.show()







#####################################

# making a wikipedia

import wikipedia

g = input("enter the word : ")
r = wikipedia.page(g)
print(r.content)




##################################


# making a calender 

import calendar 

print("the month of 2020 is : ")

print(calendar.month(2020,8))


####################################


# password generator

import random
p = random.randint(10000,30000)

username = input("enter the user name  : ")
print("hello",username)
print("here is your OTP",username,p)

password= input("enter the password")

if password==str(p):
    print("login successfully",username)

else:
    print("login failed! try again",username)



#################################################


#poetic programming


import this




##############################################


# how to extract the data using python

import PyPDF2

pdffileobj = open("C:\Users\USER\Downloads\thinkstats.pdf",'rb')

pdfReader = PyPDF2.pdfFileReader(pdffileobj)

print(PdfReader.numPages)
pageObj = PdfReader.getPage(0)
print(pageObj.extractText())
pdffileobj.close()





####################################################

# how to extract the data from websites || web scrapping



import requests
from bs4 import BeautifulSoup
link="https://www.crickbuzz.com/"
r = requests.get(link)
extract= BeautifulSoup(r.content,'html')
print(extract.prettify())



########################################################


# Guess the number using python

import random

n = random.randint(1,10)
guess = int(input("enter the number :"))

if guess==n:
    print("yes tht is correct!")
elif guess<n:
    print('your guess is low!')
else:
    print('your guess is high!')    


##########################################################

# A 3D graph technique in python

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
axis= plt.axes(projection='3d')
xposition= [1,2,3,4,5,6,7,8,9,10]
yposition= [5,6,7,8,2,5,6,3,7,2]
zposition= np.zeros(10)

dx= np.ones(10)
dy= np.ones(10)
dz= [1,2,3,4,5,6,7,8,9,10]
axis.bar3d(xposition,yposition,zposition,dx,dy,dz)
plt.show()



############################################################

# how to find the probablity of rolling die using python



from random import randint
trials = 1000
total = 0

for i in range(trials):
    if 5 in [randint(1,6) for j in range(12)]:
        total +=1
print(f"5 appears when rolling a die 12 times {total/trials:.2%}")

###########################################################

# how to merge two dictionaries in python

def mergedict(dict1,dict2):
    return(dict2.update(dict1))

dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'e':5,'f':6, 'g':7, 'h':8}
mergedict(dict1,dict2)
print(dict2)


###############################################


# how to calculate GCD using python

def gcd(x,y):
    if (y==0):
        return x
    return gcd(y,x%y)

x = int(input('enter the number:'))
y = int(input('enter the number:'))

if(gcd(x,y)):
    print("gcd of ",x,"and",y,"is", gcd(x,y))
    
else:
    print('not found enter the correct inputs')

######################################################

# how to creat a simple game in python

import random

choices = ["rock", 'paper', 'scissors']

computer = random.choice(choices)

a = input(" select rock or paper or scissors")

a = a.lower()

if a == 'rock' or 'paper' or 'scissors':
    print("the computer chooses {} and you chooses {}".format(computer,a))

    if a == 'rock':
        if computer=='rock':
            print('draw game')
        elif computer == 'paper':
            print('computer wins')
        else:
            print('you wins')
            if a == 'paper':
                if computer =='rock':
                    print('you wins')
                elif computer == 'paper':
                    print("draw game")
                else:
                    print('computer wins')
                    if user == 'scissors':
                        if computer=="rock":
                            print("computer wins")
                        elif computer=="paper":
                            print('you wins')
                        else:
                            print('game draw')
                            
                            
####################################################


# how to find LCM using python 

a = int(input("enter first num :"))
b = int(input('enter second num:'))

if (a>b):
    smallnum = a
else:
    smallnum = b
    while(1):
        if (smallnum%a==0 and smallnum%b==0):
            print("LCM of two numbers is : ", smallnum)
            break
        smallnum=smallnum+1
        
        
##########################################################


# how to find probablity of cards

import itertools,random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print('you got :')
for i in range(5):
    print(deck[i][0],'of',deck[i][1])


##############################################################

# how to findout battery % 


import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged == False : plugged == "not plugged in"
else: plugged = "plugged in"
print(percent+"percent of battery",plugged)


##############################################


# | A simple to snippet for countdown in python | |


import time
while True:
    from datetime  import datetime
    countertime = datetime.now()
    print('%s/%s/%s %s:%s:%s' % (countertime.month, countertimer.day, countertimer.year, countertimer.hour , countertimer.minute, countertimer.second ))
    time.sleep(1)


#########################################################



# | How to check your network speed in python

import pyspeedtest

speed = pyspeedtest.SpeedTest('www.google.com')
print('your ping is', speed.ping())


import pyspeedtest

speed = pyspeedtest.SpeedTest('www.facebook.com')
print('your download speed is', speed.download())


#########################################################

from spellchecker import spellchecker
spell = SpellChecker()

# find thode words tht may be misspelled

misspelledwords = spell.unknown(['lve','kng','yuth', 'rde','psd', 'jav', 'pthon'])

for word in misspelledwords:
    # get some most likely answer
    print(spell.correction(word))
    
#####################################################

# | How to find any location using python in 3 lines | 

import pygeoip

location = pygeoip.GeoIP(" location .dat file")

location.country_name_by_addr('14.137.61.12')



#########################################################

# How to find current city location in python

import pygeoip

location = pygeoip.GeoIP( '.dat file here')

location.record_by_addr('IP address')


##############################################


# How to convert any currency values in python


from currency_converter import CurrencyConverter

c = CurrencyConverter()

c.Convert(1,"INR",'KRW')


##################################################



# how to play chess in python

import chess
board = chess.Board()
print(board)


# now we move some coins
NF3 = chess.move.from_uci("g1f3")
board.push(NF3)
print(board)
# small alphabets are white 
# big alphabets are black

########################################################



# tkinter search app

from tkinter import *
# from goolge_search import search # import the search package
def search_data():
    text.delete(0.0,'end')  # it will clear the existing text
    keyword = ent.get()
    for j in search(keyword, tld = 'co.in', num=10, stop=1, pause=10):   # it produce only one result for many you can add number in it
        print(j)
    text.insert(0,0,j)
root = Tk()
root.geometry('400x100')  # gives the shape of your page

label1 = Label(root, text = "Enter") # gives the label
ent = Entry(root)   # provides text box

label1.grid(row = 0)
ent.grid(row= 0, column= 1)
button = Button(root, text = "SEARCH", bg = "lightblue")   # provides the button
button.grid(row = 2, columnspan =8)
root.mainloop()  # from the entire requirements




###########################################


# How python teaches grammer to us


from PDictionary import PyDictionary   

dictionary = PyDictionary('perception')  # enter the word tht you want to know exact meaning

print(dictionary.printMeanings())


#################################################

# how to use python as a translator

import goslate

text = "Hello World"

gs = goslate.Goslate()

translatedText = gs.translate(text, 'hi')    # 'hi'   for hindi ,, we can choose other languages also 

print(translatedText)




###################################################


 # How to get live cricket scores in python
 
 
from pycricbuzz import Cricbuzz

c = Cricbuzz()

matches = c.matches()
for match in matches:
    print(match)
    if (match['mchstate']!='nextlive'):
        print(c.livescore(match['id']))
        print(c.commentary(match['id']))
        print(c.scorecard(match['id']))
        
        
        
#########################


 # How to save RAM memory using python
 
 

import psutil
psutil.cpu_percent()  # checks current cpu units

psutil.virtual_memory()   # how much RAM we used it
dict(psutil.virtual_memory()._asdict())

####################################


# python tells a joke

import pyjokes
print(pyjokes.get_joke())

#############################


# Python Wishes you daily !!!


import datetime

now = datetime.datetime.now()

hour = now.hour

if hour<12:
    greeting=  "Good Morning"
elif hour <18:
    greeting = "Good Afternoon"
else:
    greeting= "Good NIght"
print("{}!".format(greeting))



#####################################



# How to create a colour circle using python


import turtle

colors = ["red",'purple','blue', 'green', 'orange', 'yellow']
my_pen = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    my_pen.pencolor(colors[x%6])
    my_pen.width(x/100+1)
    my_pen.forward(x)
    my_pen.left(59)


############################

#  Badword checker program using python

from profanity_check import predict,predict_prob

a = predict(['good man'])
print('AMOUNT of bad words in the string' ,a)

b = predict_prob(['fuck'])
print("percentage of badness in the string", b)

################################################


import cpuinfo
cpuinfo.get_cpu_info()['brand']


import cpuinfo
info = cpuinfo.get_cpu_info()
print(info)




import wmi
c = wmi.WMI()
for i in c.Win32_processor():
    cputype= i.Name
    print(cputype)
    
    
    
#########################################


# How to download youtube videos using python

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    you.download(['https://youtu.be/ZtDGxT-YMdg?list=PL4uwvcIXUcy2vYDwP-7g2W5r4Ha_Wqobj'])
    

###############################################



# How to check internet connection using python

from urllib.request import urlopen
def isinternetavailable():
    try:
        urlopen('http://216.58.192.142', timeout = 1)
        return True
    except:
        return False
    
print(isinternetavailable())

##############################################

# How to take screenshot using using python program

import pyautogui


im1 = pyautogui.screenshot()

im1.save('E:\screenshot.png')



#################################################


# How to create Barcode using python

import Barcodefrom barcode.writer import ImageWriter
data = "KM"
data1 = str(data)

a = barcode.get_barcode_class('code128')

b = a(data, writer = ImageWriter())

c = b.save('barcode')

########################################

