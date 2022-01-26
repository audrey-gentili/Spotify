# -*- coding: utf-8 -*-
#---------------------------TRAITEMENTS PAROLES-------------------------------#
#Nous effectuons une analyse textuelle des paroles récupérées

#paroles de chaque top
paroles_1950 = repertoire_1950.paroles()
paroles_1960 = repertoire_1960.paroles()
paroles_1970 = repertoire_1970.paroles()
paroles_1980 = repertoire_1980.paroles()
paroles_1990 = repertoire_1990.paroles()
paroles_2000 = repertoire_2000.paroles()

#paroles de toutes les chansons
paroles = repertoire.paroles()


#Nous souhaitons vérifier la langue des chansons

#détection langue
from langdetect import detect

#liste des langues détectées
langues = []
#liste des répertoires
rep = [repertoire_1950, repertoire_1960, repertoire_1970, repertoire_1980, repertoire_1990, repertoire_2000]

for r in rep: #pour chaque répertoire
    for i in r.catalogue: #pour chaque musique du répertoire
        l = detect(r.catalogue[i].paroles) #détection de la langue
        langues.append(l) #ajout de la langue dans la liste    

#Après vérification, il s'agit bien de chansons de langue anglaise
    

#Nous récupèrons l'ensemble des mots des répertoires afin d'effectuer divers traitements

print("Recuperation et traitement du vocabulaire des repertoires... \n")
#vocabulaire de chaque top
vocab_1950 = repertoire_1950.vocabulaire()
vocab_1960 = repertoire_1960.vocabulaire()
vocab_1970 = repertoire_1970.vocabulaire()
vocab_1980 = repertoire_1980.vocabulaire()
vocab_1990 = repertoire_1990.vocabulaire()
vocab_2000 = repertoire_2000.vocabulaire()

#vocabulaire global
vocab = repertoire.vocabulaire()


#Nous effectuons d'abord une lemmatisation des mots (mot à sa forme lexicale commune) avec des pos tags appropriés : natures de mots précisées

#module nltk
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

#fonction inspirée de https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/
lemmatizer = WordNetLemmatizer()

#fontion de lemmatisation selon la nature du mot (verbe, nom, etc...)
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'): #si le mot est un adjectif
        return wordnet.ADJ
    elif nltk_tag.startswith('V'): #si le mot est un verbe
        return wordnet.VERB
    elif nltk_tag.startswith('N'): #si le mot est un nom
        return wordnet.NOUN
    elif nltk_tag.startswith('R'): #si le mot est un adverbe
        return wordnet.ADV
    else:         
        return None

#fontion de lemmatisation des mots
def lemmatization(voc):
    #attribution de la nature des mots
    pos_tagged = nltk.pos_tag([i for i in voc if i])
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    #nouveau vocabulaire
    lemmatized_v = []
    #changement des mots
    for word, tag in wordnet_tagged:
        if tag is None: #s'il n'a pas trouvé de mot référent, ne change pas
            lemmatized_v.append(word)
        else:       
            #si une correspondance est trouvée, remplace par celle-là
            lemmatized_v.append(lemmatizer.lemmatize(word, tag))
    #rangement dans l'ordre croissant
    lemmatized_v = sorted(lemmatized_v)
    return lemmatized_v

#appels de la fonction lemmatization pour chaque vocabulaire
vocab = lemmatization(vocab)
vocab_1950 = lemmatization(vocab_1950)
vocab_1960 = lemmatization(vocab_1960)
vocab_1970 = lemmatization(vocab_1970)
vocab_1980 = lemmatization(vocab_1980)
vocab_1990 = lemmatization(vocab_1990)
vocab_2000 = lemmatization(vocab_2000)


#Nous sélectionnons ensuite les mots issus d'un dictionnaire anglais et supprimons les mots-outils

#module
import pandas as pd 

#liste de mots-outils et dictionnaire à partir d'un fichier CSV
outils = pd.read_csv("outils.csv", sep=";")
#récupération des mots-outils dans une liste
mots = outils['Outils'].values.tolist()
#récupération du dictionnnaire dans une liste
dico = outils['Dico'].values.tolist()
#suppression des valeurs nulles
outils = [x for x in mots if pd.isnull(x) != True]

#module calcul de fréquences
from collections import Counter

#fonction de récupération des mots du dictionnaire anglais et suppression des mots-outils
def dictionnaire(voc):
    nouveau_vocab = [] #nouveau vocabulaire
    for mot in voc:
        for m in dico:
            if (mot == m): #si le mot est dans le dictionnaire
                nouveau_vocab.append(mot) #ajout du mot            
    for mot in outils:
        for m in nouveau_vocab:
            if (mot == m): #si le mot est dans la liste outils
                nouveau_vocab.remove(m) #suppression du mot
    freq = Counter(nouveau_vocab) #fréquence d'apparition des mots
    nouveau_vocab = sorted(list(set(nouveau_vocab))) #tri par ordre croissant des mots uniques
    return nouveau_vocab, freq


#En raison d'un temps d'exécution de la fonction dictionnaire() très important,
#nous avons choisi de ne l'appeler qu'une seule fois et de stocker ces résultats dans des fichiers .txt
'''       
#appels de la fonction dictionnaire pour les nouveaux vocabulaires
n_vocab, fvocab = dictionnaire(vocab)
n_vocab_1950, fvocab_1950 = dictionnaire(vocab_1950)
n_vocab_1960, fvocab_1960 = dictionnaire(vocab_1960)
n_vocab_1970, fvocab_1970 = dictionnaire(vocab_1970)
n_vocab_1980, fvocab_1980 = dictionnaire(vocab_1980)
n_vocab_1990, fvocab_1990 = dictionnaire(vocab_1990)
n_vocab_2000, fvocab_2000 = dictionnaire(vocab_2000)
'''

#module pickle
import pickle

'''
#création de fichiers txt pour stocker les vocabulaires
with open("vocab.txt", "wb") as fp:
    pickle.dump(n_vocab, fp)
with open("vocab_1950.txt", "wb") as fp:
    pickle.dump(n_vocab_1950, fp)
with open("vocab_1960.txt", "wb") as fp:
    pickle.dump(n_vocab_1960, fp)
with open("vocab_1970.txt", "wb") as fp:
    pickle.dump(n_vocab_1970, fp)
with open("vocab_1980.txt", "wb") as fp:
    pickle.dump(n_vocab_1980, fp)
with open("vocab_1990.txt", "wb") as fp:
    pickle.dump(n_vocab_1990, fp)
with open("vocab_2000.txt", "wb") as fp:
    pickle.dump(n_vocab_2000, fp)

#création de fichiers txt pour stocker les fréquences
with open("fvocab.txt", "wb") as fp:
    pickle.dump(fvocab, fp)
with open("fvocab_1950.txt", "wb") as fp:
    pickle.dump(fvocab_1950, fp)
with open("fvocab_1960.txt", "wb") as fp:
    pickle.dump(fvocab_1960, fp)
with open("fvocab_1970.txt", "wb") as fp:
    pickle.dump(fvocab_1970, fp)
with open("fvocab_1980.txt", "wb") as fp:
    pickle.dump(fvocab_1980, fp)
with open("fvocab_1990.txt", "wb") as fp:
    pickle.dump(fvocab_1990, fp)
with open("fvocab_2000.txt", "wb") as fp:
    pickle.dump(fvocab_2000, fp)
'''

#récupération des fichiers txt
with open("vocab.txt", "rb") as fp:
    n_vocab = pickle.load(fp)
with open("vocab_1950.txt", "rb") as fp:
    n_vocab_1950 = pickle.load(fp)
with open("vocab_1960.txt", "rb") as fp:
    n_vocab_1960 = pickle.load(fp)
with open("vocab_1970.txt", "rb") as fp:
    n_vocab_1970 = pickle.load(fp)
with open("vocab_1980.txt", "rb") as fp:
    n_vocab_1980 = pickle.load(fp)
with open("vocab_1990.txt", "rb") as fp:
    n_vocab_1990 = pickle.load(fp)
with open("vocab_2000.txt", "rb") as fp:
    n_vocab_2000 = pickle.load(fp)
with open("fvocab.txt", "rb") as fp:
    fvocab = pickle.load(fp)
with open("fvocab_1950.txt", "rb") as fp:
    fvocab_1950 = pickle.load(fp)
with open("fvocab_1960.txt", "rb") as fp:
    fvocab_1960 = pickle.load(fp)
with open("fvocab_1970.txt", "rb") as fp:
    fvocab_1970 = pickle.load(fp)
with open("fvocab_1980.txt", "rb") as fp:
    fvocab_1980 = pickle.load(fp)
with open("fvocab_1990.txt", "rb") as fp:
    fvocab_1990 = pickle.load(fp)
with open("fvocab_2000.txt", "rb") as fp:
    fvocab_2000 = pickle.load(fp)
    

#---------------------------MATRICE INDEX DES MOTS----------------------------#
#Nous effectuons ici une matrice termes-documents pour les mots des paroles des chansons

#module
import numpy as np

print("\nCreation de la matrice d'index du vocabulaire... \n")
#vocabulaire global
vocab = n_vocab

#liste des vocabulaires de chaque top
dico = [n_vocab_1950, n_vocab_1960, n_vocab_1970, n_vocab_1980, n_vocab_1990, n_vocab_2000]
#liste des fréquences de chaque top 
freq = [fvocab_1950, fvocab_1960, fvocab_1970, fvocab_1980, fvocab_1990, fvocab_2000]  

m = 6 #nombre de tops
n = len(vocab) #nombre de mots
index_mots = np.zeros((m,n)) #création de la matrice des index

for i, mot in enumerate(vocab): #pour chaque mot du vocabulaire global
    for d in range(6):
        for j in dico[d]: #pour chaque mot du vocabulaire du top
            if (mot == j): #si le mot est dans le vocabulaire du top
                index_mots[d][i] = freq[d][mot] #ajout de la fréquence

#conversion des index en entiers
index_mots = index_mots.astype(int)

#conversion de la matrice en dataframe pandas
df_mots = pd.DataFrame(index_mots)
#mots du vocabulaire en noms de colonnes
df_mots.columns = vocab
#années des tops en noms de lignes
df_mots.rename(index = {0: '1950', 1: '1960', 2: '1970', 3: '1980', 4: '1990', 5: '2000'}, inplace = True)

#création d'un fichier CSV pour stocker l'index
df_mots.to_csv("df_mots.csv", sep=';')


#----------------------------TRAITEMENTS GENRES-------------------------------#
#Nous récupérons ici les genres et leur fréquence avec les méthodes établies dans la classe Repertoire

print("Recuperation des genres musicaux des repertoires... \n")
#genres de chaque top
genres_1950, dico_1950, freq_1950 = repertoire_1950.nouveaux_genres()
genres_1960, dico_1960, freq_1960 = repertoire_1960.nouveaux_genres()
genres_1970, dico_1970, freq_1970 = repertoire_1970.nouveaux_genres()
genres_1980, dico_1980, freq_1980 = repertoire_1980.nouveaux_genres()
genres_1990, dico_1990, freq_1990 = repertoire_1990.nouveaux_genres()
genres_2000, dico_2000, freq_2000 = repertoire_2000.nouveaux_genres()

#genres de tous les artistes
all_genres, dico_genres, freq_genres = repertoire.nouveaux_genres()


#--------------------------MATRICE INDEX DES GENRES---------------------------#
#Nous effectuons ici une matrice termes-documents pour les genres musicaux

print("Creation de la matrice d'index des genres musicaux... \n")
#tous les genres
dico_genres = sorted(list(dico_genres))

#liste des genres de chaque top
dico = [sorted(list(dico_1950)), sorted(list(dico_1960)), sorted(list(dico_1970)), sorted(list(dico_1980)), sorted(list(dico_1990)), sorted(list(dico_2000))]  
#liste des fréquences de chaque top 
freq = [freq_1950, freq_1960, freq_1970, freq_1980, freq_1990, freq_2000] 

m = 6 #nombre de tops
n = len(dico_genres) #nombre de genres
index_genres = np.zeros((m,n)) #création de la matrice des index

for i, genre in enumerate(dico_genres): #pour chaque genre du dictionnaire global
    for d in range(6):
        for j in dico[d]: #pour chaque genre du dictionnaire du top
            if (genre == j): #si le genre est dans le dictionnaire du top
                index_genres[d][i] = freq[d][genre] #ajout de la fréquence dans la matrice 

#conversion des index en entiers
index_genres = index_genres.astype(int)

#conversion de la matrice en dataframe pandas
df_genres = pd.DataFrame(index_genres)
#mots du vocabulaire en noms de colonnes
df_genres.columns = dico_genres
#années des tops en noms de lignes
df_genres.rename(index = {0: '1950', 1: '1960', 2: '1970', 3: '1980', 4: '1990', 5: '2000'}, inplace = True)

#création d'un fichier CSV pour stocker l'index
df_genres.to_csv("df_genres.csv", sep=';')


#---------------------------TRAITEMENTS ARTISTES------------------------------#
#Nous récupérons ici les artistes et leur fréquence avec les méthodes établies dans la classe Repertoire

print("Recuperation des artistes des repertoires... \n")
#artistes de chaque top et leur fréquence
artistes_1950 = repertoire_1950.all_artistes()
dico_a_1950, freq_a_1950 = repertoire_1950.dico_artistes()
artistes_1960 = repertoire_1960.all_artistes()
dico_a_1960, freq_a_1960 = repertoire_1960.dico_artistes()
artistes_1970 = repertoire_1970.all_artistes()
dico_a_1970, freq_a_1970 = repertoire_1970.dico_artistes()
artistes_1980 = repertoire_1980.all_artistes()
dico_a_1980, freq_a_1980 = repertoire_1980.dico_artistes()
artistes_1990 = repertoire_1990.all_artistes()
dico_a_1990, freq_a_1990 = repertoire_1990.dico_artistes()
artistes_2000 = repertoire_2000.all_artistes()
dico_a_2000, freq_a_2000 = repertoire_2000.dico_artistes()

#artistes de toutes les chansons
all_artistes = repertoire.all_artistes()
dico_artistes, freq_artistes = repertoire.dico_artistes()


#--------------------------MATRICE INDEX DES ARTISTES-------------------------#
#Nous effectuons ici une matrice termes-documents pour les artistes

print("Creation de la matrice d'index des artistes... \n")
#tous les artistes
dico_artistes = sorted(list(dico_artistes))

#liste des artistes de chaque top
dico = [sorted(list(dico_a_1950)), sorted(list(dico_a_1960)), sorted(list(dico_a_1970)), sorted(list(dico_a_1980)), sorted(list(dico_a_1990)), sorted(list(dico_a_2000))]
#liste des fréquences de chaque top 
freq_artistes = [freq_a_1950, freq_a_1960, freq_a_1970, freq_a_1980, freq_a_1990, freq_a_2000]

m = 6 #nombre de tops
n = len(dico_artistes) #nombre d'artistes
index_artistes = np.zeros((m,n)) #création de la matrice des index

for i, artiste in enumerate(dico_artistes): #pour chaque artiste du dictionnaire global
    for d in range(6):
        for j in dico[d]: #pour chaque artiste du dictionnaire du top
            if (artiste == j): #si l'artiste est dans le dictionnaire du top
                index_artistes[d][i] = freq_artistes[d][artiste] #ajout de la fréquence dans la matrice 

#conversion des index en entiers
index_artistes = index_artistes.astype(int)

#conversion de la matrice en dataframe pandas
df_artistes = pd.DataFrame(index_artistes)
#mots du vocabulaire en noms de colonnes
df_artistes.columns = dico_artistes
#années des tops en noms de lignes
df_artistes.rename(index = {0: '1950', 1: '1960', 2: '1970', 3: '1980', 4: '1990', 5: '2000'}, inplace = True)

#création d'un fichier CSV pour stocker l'index
df_artistes.to_csv("df_artistes.csv", sep=';')