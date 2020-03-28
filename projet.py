# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import webbrowser
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import spacy
from lxml import html
import requests
from bs4 import BeautifulSoup
nlp = spacy.load("fr_core_news_sm")
'''
def speak(text):
	tts = gTTS(text=text, lang="fr")
	filename="voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Je vous ecoute :")
	    audio = r.listen(source)
	    try:
	        text = r.recognize_google(audio, language="fr-FR")
	        print("Vous avez dit : {}".format(text))
	    except:
	        print("Je ne comprends pas")

	    return text


speak("Bonjour, je suis Ester votre assistant vocal. Que puis-je faire pour vous ?")
text = get_audio()
'''
def recherche(text):
	doc = nlp(text)
	#recherche google
	p = "PROPN"
	n = "NOUN"
	v = "VERB"
	recherche = []
	i=0
	for X in doc:
		if X.pos_ == p or X.pos_ == n or X.pos_ == v:
			#print(X, X.pos_)
			#print(X)
			recherche.insert(i, str(X))
			i=i+1

	envoierecherche = ' '.join(recherche)
	url="https://news.google.com/search?q="+envoierecherche+"&hl=fr&gl=FR&ceid=FR%3Afr"
	#print(url)
	recherche_titre(url)
	webbrowser.open(url)

def recherche_titre(url):
	######## Recherche le titre 1er article ########
	requete = requests.get(url)
	page = requete.content
	soup = BeautifulSoup(page, 'html.parser')
	mydivs = soup.find("a", {"class": "DY5T1d"})
	print(mydivs.get_text())



text = ("que faut il manger en hiver")
recherche(text)

