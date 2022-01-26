# -*- coding: utf-8 -*-
#---------------------------CREATION DES OBJETS-------------------------------#
#Nous créons ici les objets de la classe Musique et les mettons dans un catalogue

from Classes import Musique

#tops et musiques récupérés
tops = {'1950':tracks_1950, '1960':tracks_1960, '1970':tracks_1970, '1980':tracks_1980, '1990':tracks_1990, '2000':tracks_2000}
#catalogue des musiques
catalogue = [] 

#création de la liste des musiques
for nom_top,top in tops.items(): #pour chaque top
    for song in top: #pour chaque musique
        titre = song[0] #récupération du titre
        album = song[1] #récupération de l'album
        artiste = song[2] #récupération de l'artiste
        genre = song[3] #récupération des genres musicaux de l'artiste
        date = song[4] #récupération de la date
        duree = song[5] #récupération de la durée
        top = nom_top #récupération de l'année du top
        musique = Musique(titre, album, artiste, genre, date, duree, top) #création de l'objet musique
        catalogue.append(musique) #ajout de la musique au catalogue

#index du catalogue
index_cat = {}
for i, song in enumerate(catalogue):
    index_cat[i] = song.titre   
    

#Nous créons ici les objets de la classe Artiste et les mettons dans un dictionnaire

from Classes import Artiste

#dictionnaire des artistes
artistes = {}
#index des artistes
index_art = {}
#nombre d'artistes
nart = 0

#création du dictionnaire des artistes
for song in catalogue: #pour chaque musique
    if song.artiste not in index_art: #si l'artiste n'est pas dans l'index
        nart += 1 #nombre d'artistes
        artistes[nart] = Artiste(song.artiste, song.genre) #création de l'objet artiste
        index_art[song.artiste] = nart #création de l'index
    if song.titre not in artistes[index_art[song.artiste]].repertoire: #si le titre n'est pas dans le répertoire musical
        artistes[index_art[song.artiste]].add(song.titre) #ajout d'une chanson dans le répertoire de l'artiste
        
        
#------------------------------POLYMORPHISME----------------------------------#
#Nous utilisons l'héritage pour créer les objets de la classe MusiqueAvecParoles, dont la classe-mère est Musique

from Classes import MusiqueAvecParoles

#module
import re

#tops et paroles récupérés
lyrics = {'1950':lyrics_1950, '1960':lyrics_1960, '1970':lyrics_1970, '1980':lyrics_1980, '1990':lyrics_1990, '2000':lyrics_2000}

#catalogue des musiques avec paroles
catalogue_par = [] 

for nom_top, lyric in lyrics.items(): #pour chaque top
    for i in range(len(lyric)): #pour chaque musique du top
        for musique in catalogue: #pour chaque musique du catalogue
            if ((lyric[1][i] == musique.titre) and (nom_top == musique.top)): #si la musique possède des paroles
                paroles = lyric[3][i] #récupération des paroles de la musique      
                paroles = re.sub("[0-9]{0,2}EmbedShare URLCopyEmbedCopy", '', paroles) #suppression de l'information en surplus à la fin des paroles
                m = MusiqueAvecParoles(titre=musique.titre, album=musique.album, artiste=musique.artiste, genre=musique.genre, date=musique.date, duree=musique.duree, top=musique.top, paroles=paroles) #création de l'objet musiqu
                catalogue_par.append(m) #ajout de la musique au catalogue
                

#--------------------------------REPERTOIRES----------------------------------#
#Nous créons les objets de la classe Repertoire afin d'obtenir nos différents répertoires musicaux

print("Creation des repertoires musicaux... \n")
from Repertoire import Repertoire

#création de répertoires par année
repertoire_1950 = Repertoire("Repertoire musical top 1950")
repertoire_1960 = Repertoire("Repertoire musical top 1960")
repertoire_1970 = Repertoire("Repertoire musical top 1970")
repertoire_1980 = Repertoire("Repertoire musical top 1980")
repertoire_1990 = Repertoire("Repertoire musical top 1990")
repertoire_2000 = Repertoire("Repertoire musical top 2000")

#création du répertoire global
repertoire = Repertoire("Repertoire musical global")

#ajout des chansons au répertoire correspondant
for musique in catalogue_par:
    if (musique.top == '1950'):
        repertoire_1950.add(musique)
        repertoire.add(musique)
    elif (musique.top == '1960'):
        repertoire_1960.add(musique)
        repertoire.add(musique)
    elif (musique.top == '1970'):
        repertoire_1970.add(musique)
        repertoire.add(musique)
    elif (musique.top == '1980'):
        repertoire_1980.add(musique)
        repertoire.add(musique)
    elif (musique.top == '1990'):
        repertoire_1990.add(musique)
        repertoire.add(musique)
    elif (musique.top == '2000'):
        repertoire_2000.add(musique)
        repertoire.add(musique)