#--------------------------------REPERTOIRE-----------------------------------#
import re 
from collections import Counter
from Classes import Artiste

class Repertoire:
    #constructeur
    #initialisation des attributs de la classe
    def __init__(self, nom):
        self.nom = nom #nom du répertoire
        self.artistes = {} #artiste du répertoire
        self.index_art = {} #index des artiste
        self.catalogue = {} #chansons du répertoire
        self.nsong = 0 #nombre de chansons
        self.nart = 0 #nombre d'artistes

    #méthode d'ajout
    def add(self, musique):
        if musique.artiste not in self.index_art: #si l'artiste n'est pas présent dans l'index
            self.nart += 1 #incrémentation du nombre d'artistes
            self.artistes[self.nart] = Artiste(musique.artiste, musique.genre) #création d'un objet Artiste
            self.index_art[musique.artiste] = self.nart #index de l'artiste
        self.artistes[self.index_art[musique.artiste]].add(musique.titre) #ajout du titre à l'artiste
        self.nsong += 1 #incrémentation du nombre de chansons
        self.catalogue[self.nsong] = musique #ajout de la musique au catalogue

    #méthode d'affichage
    def __repr__(self):
        song = list(self.catalogue.values()) #récupération des chansons du catalogue
        song = list(sorted(song, key=lambda x: x.titre)) #tri croissant
        return "\n".join(list(map(str, song)))
    

#--------------------------méthodes calcul moyennes---------------------------#
    #méthode de calcul du nombre de mots moyen du répertoire
    def nombre_mots(self):
        mots = [] #liste du nombre de mots
        paroles = "" #longue chaine de caractères pour les paroles
        for i in self.catalogue: #pour chaque chanson du répertoire
             paroles = str.lower(self.catalogue[i].paroles) #paroles en minuscules
             paroles = re.sub("[0-9\-\?\!:\(\)\"\.,\$\\\]*","",paroles) #suppression des caractères spéciaux
             paroles = paroles.split(" ") #séparation des paroles pour chaque mot
             mots.append(len(paroles)) #ajout du nombre de mots
        moyenne = sum(mots)/len(mots) #calcul de la moyenne des mots
        return moyenne
    
    #méthode de calcul de la durée moyenne des chansons du répertoire
    def duree(self):
        durees = [] #liste des durées
        for i in self.catalogue: #pour chaque chanson du répertoire
            durees.append(self.catalogue[i].duree) #ajout de la durée de la chanson
        moyenne = sum(durees)/len(durees) #calcul de la moyenne des durées
        return moyenne
   
#----------------------méthodes traitements paroles---------------------------#
    #méthode de récupération des paroles du répertoire
    def paroles(self):
        allparoles = "" #longue chaine de caractères des paroles
        for i in self.catalogue: #pour chaque chanson
            allparoles += " "+str.lower(self.catalogue[i].paroles) #ajout des paroles en minuscules
        allparoles = re.sub("[0-9\-\?\!:\(\)\"\.,\$\\\]*","",allparoles) #suppression des caractères spéciaux
        return allparoles
    
    #méthode de récupération du vocabulaire unique du répertoire
    def dico_vocabulaire(self):
        allparoles = self.paroles() #appel de la méthode paroles()
        allparoles = allparoles.split(" ") #séparation des paroles pour chaque mot
        vocabulaire = set() #ensemble du vocabulaire
        for i in range(len(allparoles)): #pour chaque mot
            vocabulaire.add(allparoles[i]) #ajout du mot au vocabulaire
        vocabulaire.discard(' ') #suppression de l'élément vide dans le vocabulaire
        return sorted(vocabulaire)
    
    #méthode de récupération du vocabulaire du répertoire et de sa fréquence
    def vocabulaire(self):
        allparoles = self.paroles() #appel de la méthode paroles()
        allparoles = allparoles.split(" ") #séparation des paroles pour chaque mot
        vocabulaire = [] #liste des mots
        for i in range(len(allparoles)): #pour chaque mot
            vocabulaire.append(allparoles[i]) #ajout du mot à la liste
        return sorted(vocabulaire)

#-----------------------méthodes traitements genres---------------------------#
    #méthode de récupération des genres musicaux du répertoire
    def genres(self):
        genres = [] #liste des genres
        for i in self.catalogue: #pour chaque chanson
            for genre in self.catalogue[i].genre: #pour chaque genre musical de l'artiste
                genres.append(genre) #ajout du genre
        return genres
    
    #méthode de récupération de la fréquence des genres du répertoire
    def frequence_genres(self):
        genres = self.genres() #appel de la méthode genres()
        freq = Counter(genres) #fréquence d'apparition des genres
        return freq
    
    #méthode de modification des genres du répertoire et de récupération de leur fréquence
    def nouveaux_genres(self):
        genres = self.genres() #appel de la méthode genres()
        fgenres = self.frequence_genres() #appel de la méthode frequence_genres()
        #genres les plus connus
        mots = ['pop', 'rap', 'rock', 'hip hop', 'metal', 'folk', 'country', 'soul', 'jazz', 'r&b', 'disco', 'blues', 'funk', 'reggae']
        for i in range(len(genres)): #pour chaque genre du répertoire
            if (fgenres[genres[i]] < 10): #si le genre apparait moins de 10 fois
                for mot in mots: #pour chaque genre connu
                    if (mot in genres[i]): #si le genre contient un genre connu
                        genres[i] = mot #remplacement du genre par le genre connu
        freq = Counter(genres) #fréquence d'apparition des nouveaux genres
        for cle in freq: #pour chaque genre unique
            if (freq[cle] < 5): #si le genre apparait moins de 5 fois
                for i in range(freq[cle]): #pour chaque apparition du genre
                    genres.remove(cle) #suppression du genre
        dico_genres = set(genres) #ensemble des nouveaux genres uniques
        freq = Counter(genres) #frequence d'apparition des nouveaux genres
        return genres, dico_genres, freq
    
#---------------------méthodes traitements artistes---------------------------#
    #méthode de récupération des artistes du répertoire
    def all_artistes(self):
        artistes = [] #liste des genres
        for i in self.catalogue: #pour chaque chanson
                artistes.append(self.catalogue[i].artiste) #ajout de l'artiste à la liste
        return artistes
    
    #méthode de récupération des artistes uniques du répertoire et de leur fréquence
    def dico_artistes(self):
        artistes = self.all_artistes() #appel de la méthode all_artistes()
        freq = Counter(artistes) #frequence d'apparition des artistes
        allartistes = set() #ensemble des artistes uniques
        for i in self.artistes: #pour chaque artiste
                allartistes.add(self.artistes[i].artiste) #ajout de l'artiste
        return allartistes, freq