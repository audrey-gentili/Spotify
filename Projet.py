# -*- coding: utf-8 -*-
"""
@authors: Martelet-Thomas Sophie et Gentili Audrey                                                                      
                                                                         
"""

#-----------------------------EXECUTION DES SCRIPTS---------------------------#
exec(open("Recuperation.py").read()) #fichier .py de récupération des chansons et de leurs paroles
exec(open("Objets.py").read()) #fichier .py de création des objets issus des classes
exec(open("Traitements.py").read()) #fichier .py de traitements des données et de création des matrices d'index


#----------------------------INTERFACE ET ANALYSES----------------------------#
#Nous faisons appel à la librairie Tkinter afin de créer une interface visuelle

#librairies
import tkinter as tk

#Nous créons d'abord une page d'accueil d'explication du projet

#création de l'accueil de l'interface Tkinter
root = tk.Tk()
root.title('Accueil')

#taille de l'écran d'ordinateur pour ajuster la fenêtre
width = root.winfo_screenwidth()  
height = root.winfo_screenheight() 
root.geometry("%dx%d" % (width, height)) 


#Nous créons ensuite une sous-fenêtre appartenant à la fenêtre accueil pour chaque objet d'analyse

#fenêtre d'affichage des moyennes
app = tk.Toplevel(root)
app.title('Données et moyennes')
app.geometry("%dx%d" % (width, height)) 

#fenêtre d'affichage des analyses sur les artistes
app1 = tk.Toplevel(root)
app1.title('Analyse des artistes')
app1.geometry("%dx%d" % (width, height)) 

#fenêtre d'affichage des analyses sur les artistes
app1bis = tk.Toplevel(root)
app1bis.title('Analyse des artistes - Suite')
app1bis.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des analyses sur les genres
app2 = tk.Toplevel(root)
app2.title('Analyse des genres')
app2.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des analyses sur les genres
app2bis = tk.Toplevel(root)
app2bis.title('Analyse des genres - Suite')
app2bis.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des analyses sur les mots
app3 = tk.Toplevel(root)
app3.title('Analyse des mots')
app3.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots du vocabulaire
app4 = tk.Toplevel(root)
app4.title('Nuages de mots du vocabulaire des tops 1950, 1960 et 1970')
app4.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots du vocabulaire
app4bis = tk.Toplevel(root)
app4bis.title('Nuages de mots du vocabulaire des tops 1980, 1990 et 2000')
app4bis.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots des artistes
app5 = tk.Toplevel(root)
app5.title('Nuages de mots des artistes des tops 1950, 1960 et 1970')
app5.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots des artistes
app5bis = tk.Toplevel(root)
app5bis.title('Nuages de mots des artistes des tops 1980, 1990 et 2000')
app5bis.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots des genres
app6 = tk.Toplevel(root)
app6.title('Nuages de mots des genres des tops 1950, 1960 et 1970')
app6.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots des genres
app6bis = tk.Toplevel(root)
app6bis.title('Nuages de mots des genres des tops 1980, 1990 et 2000')
app6bis.geometry("%dx%d" % (width, height))

#fenêtre d'affichage des nuages de mots globaux
app7 = tk.Toplevel(root)
app7.title('Nuages de mots')
app7.geometry("%dx%d" % (width, height))


#Nous intégrons des boutons en haut de chaque fenêtre pour permettre la navigation entre chacune d'elle

#bouton d'affichage de la fenêtre suivante
button = tk.Button(root, text="DEMARRER", bg="#9AE595", command=app.lift)
button.pack()
#bouton de fermeture de l'interface
button = tk.Button(root, text="FERMER", bg="#F38070", command=root.destroy)
button.pack()


#Nous intégrons du texte aux fenêtres grâce aux Labels

#messages d'affichage
message = tk.Label(root, text="Projet programmation Python :\n Algorithmie et Programmation Avancée\n")
message.configure(font="bold")
message.pack()
message = tk.Label(root, text="Analyse des playlists des tops de Spotify par décennie \n Par Martelet-Thomas Sophie et Gentili Audrey\n")
message.configure(font="bold")
message.pack()

message = tk.Label(root, text="\nNous avons sélectionné les playlists “All Out” de Spotify pour les années 50, 60, 70, 80, 90 et 2000.\nCes playlists sont composées du top 150 des chansons les plus écoutées de la décennie.")
message.configure(font="bold")
message.pack()

message = tk.Label(root, text="\n\nNombre de chansons et d'artistes récupérés :")
message.pack()

#modules
import pandas as pd
import numpy as np

#Nous établissons et affichons un dataframe récapitulant le nombre de données recueillies

#tableau du nombre de chansons et d'artistes pour chaque top
ar = np.array([[repertoire_1950.nsong,repertoire_1960.nsong,repertoire_1970.nsong,repertoire_1980.nsong,repertoire_1990.nsong,repertoire_2000.nsong],
              [repertoire_1950.nart,repertoire_1960.nart,repertoire_1970.nart,repertoire_1980.nart,repertoire_1990.nart,repertoire_2000.nart]])
#conversion du tableau en dataframe
df = pd.DataFrame(ar, index=['Nombres de chansons', 'Nombres d\'artistes'], columns=['1950', '1960', '1970', '1980', '1990', '2000'])

#affichage du dataframe
message = tk.Label(root, text=df)
message.pack()


#----------------------------Données d'analyse--------------------------------#
#Nous effectuons des analyses sur le nombre de mots des chansons et leur durée

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app, text="SUIVANT", bg="#9AE595", command=app1.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app, text="PRECEDENT", bg="#F8DD96", command=root.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#-----------------------------Nombre de mots----------------------------------#
#nombre de mots moyen pour chaque top
nbmots_1950 = repertoire_1950.nombre_mots()
nbmots_1960 = repertoire_1960.nombre_mots()
nbmots_1970 = repertoire_1970.nombre_mots()
nbmots_1980 = repertoire_1980.nombre_mots()
nbmots_1990 = repertoire_1990.nombre_mots()
nbmots_2000 = repertoire_2000.nombre_mots()

#tuple des moyennes
n = (int(nbmots_1950), int(nbmots_1960), int(nbmots_1970), int(nbmots_1980), int(nbmots_1990), int(nbmots_2000))

#nombre de mots moyen
nbmots = repertoire.nombre_mots()

message = tk.Label(app, text="\nNotre premier traitement consiste à trouver le nombre de mots moyen pour savoir si le lexique utilisé se développe au fil du temps : \n")
message.pack()

message = tk.Label(app, text="Nombre de mots moyen dans chaque top par chanson : ")
message.pack()
date = 1950

for i in range (0,6): #pour chaque top
    #affichage du nombre de mots moyen pour chaque top
    message = tk.Label(app, text=str(date)+" : "+str(n[i])+" mots.")
    message.pack()
    date = date + 10 #passage au top suivant
#affichage du nombre de mots moyen global
message = tk.Label(app, text="En moyenne globale : "+ str(int(nbmots))+" mots. \n")
message.pack()

message = tk.Label(app, text=" => Ainsi, le nombre de mots augmente bien au fur et à mesure : il a plus que doublé en 50 ans.")
message.pack()


#Nous visualisons ces résultats dans un graphique

message = tk.Label(app, bg="#88D1FF", text="Une courbe représentant ces données est disponible dans la fenêtre plots de votre environnement python.\n")
message.pack()

#librairie
import matplotlib.pyplot as plt

plt.plot(n) #création du graphique
plt.title("Comparatif du nombre de mots uniques entre 1950 et 2000")
plt.show() #affichage du graphique

#----------------------------------Durée--------------------------------------#
#durée moyenne pour chaque top
duree_1950 = repertoire_1950.duree()
duree_1960 = repertoire_1960.duree()
duree_1970 = repertoire_1970.duree()
duree_1980 = repertoire_1980.duree()
duree_1990 = repertoire_1990.duree()
duree_2000 = repertoire_2000.duree()

#tuple des moyennes
d = (duree_1950, duree_1960, duree_1970, duree_1980, duree_1990, duree_2000)

#durée moyenne globale
duree = repertoire.duree()

message = tk.Label(app, text="\nNotre second traitement consiste à faire la même chose pour la durée des chansons :")
message.pack()

message = tk.Label(app, text="Durée moyenne d'une chanson dans chaque top : ")
message.pack()
date = 1950
for i in range (0,6):#pour chaque top
    #affichage de la durée moyenne pour chaque top
    message = tk.Label(app, text=str(date)+" : "+str(round(d[i], 2))+" minutes.")
    message.pack()
    date = date + 10 #passage au top suivant
#affichage de la durée moyenne globale
message = tk.Label(app, text="En moyenne globale : "+str(round(duree, 2))+" minutes. \n")
message.pack()

message = tk.Label(app, text=" => Ainsi, la durée augmente au fur et à mesure, un peu moins vite que le nombre de mots.")
message.pack()


#Nous visualisons ces résultats dans un graphique

message = tk.Label(app, bg="#88D1FF", text="Une courbe représentant ces données est disponible dans la fenêtre plots de votre environnement python.\n")
message.pack()

plt.plot(d) #création du graphique
plt.title("Comparatif des durées des chansons entre 1950 et 2000")
plt.show() #affichage du graphique     

#----------------------------Comparaison des deux-----------------------------#
message = tk.Label(app, text="=> Nous remarquons une augmentation au fil du temps du nombre de mots et de la durée. \n Les deux variables sont-elles corrêlées ?")
message.pack()

#Est-ce que la durée et le nombre de mots moyens sont corrélés ? 
#Si durée importante alors nb de mots importants ? Si nb de mots grands alors durée longue ? 
coef = np.corrcoef(n, d)
message = tk.Label(app, text=coef)
message.pack()

message = tk.Label(app, text="La matrice des coefficients montre que non, le coefficient est seulement de {:.2f}. \n".format(np.corrcoef(n, d)[1,0]))
message.pack()
#coefficient de 0,66, pas très sûr comme liaison

#Nous visualisons ces résultats dans un nuage de ponts

plt.scatter(n, d) #création du nuage de points
plt.title("Nuage de points entre durée et nombre de mots")
plt.show() #affichage du nuage de points

message = tk.Label(app, bg="#88D1FF", text="Un nuage de points entre ces deux variables est disponible dans la fenêtre plots de votre environnement python.")
message.pack()

message = tk.Label(app, text=" => Il est visible que lorsque la durée augmente, le nombre de mots n'augmente pas forcément et inversement.\n")
message.pack()


#------------------------Artistes dans plusieurs tops-------------------------#
#Nous effectuons par la suite des analyses sur les artistes

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app1, text="SUIVANT", bg="#9AE595", command=app1bis.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app1, text="PRECEDENT", bg="#F8DD96", command=app.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app1, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#artistes présents dans plusieurs tops
c = 0 #compteur artistes
c2 = 0 #compteur artistes 2 tops
c3 = 0 #compteur artistes 3 tops
c4 = 0 #compteur artistes 4 tops
c5 = 0 #compteur artistes 5 tops
c6 = 0 #compteur artistes 6 tops
top = list()
art = list()
top_total = []
nrow = index_artistes.shape[0] #nombre de lignes de la matrice d'index
ncol = index_artistes.shape[1] #nombre de colonnes de la matrice d'index

message = tk.Label(app1, text="\nLa seconde étape est de voir quels sont les artistes qui reviennent dans plusieurs tops : ceux qui sont donc très populaires sur plus de dix ans :\n")
message.pack()

message = tk.Label(app1, text="Tous ces artistes reviennent dans plusieurs tops :")
message.pack()

for i in range(ncol): #pour chaque artiste
    for j in range (nrow): #pour chaque top
        if (index_artistes[j][i] != 0): #si l'artiste est présent dans le top
            c += 1 #incrémentation du compteur
            nom_top = str(1950 + j * 10) #récupération du top
            top.append(int(nom_top)) #ajout du top à la liste
    if (c > 1): #si l'artiste apparait dans plusieurs tops
        art.append(i) #ajout de l'artiste à la liste
        #affichage des résultats dans l'interface
        message = tk.Label(app1, text=str(dico_artistes[i])+" apparait dans "+str(c)+" tops : "+str(top)+".  ")
        message.pack()
        top_total.append(tuple(top)) #ajout des tops à la liste
        #incrémentations des compteurs en fonction de la présence de l'artiste
        if (c == 2):
            c2 += 1
        elif(c == 3):
            c3 += 1
        elif (c == 4):
            c4 += 1
        elif (c == 5):
            c5 += 1
        else: 
            c6 += 1
    #réinitialisation des variables
    c = 0
    top = list()

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app1bis, text="SUIVANT", bg="#9AE595", command=app2.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app1bis, text="PRECEDENT", bg="#F8DD96", command=app1.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app1bis, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

message = tk.Label(app1bis, text="\nSont présentés ci-dessous dans combien de tops reviennent les artistes qui sont présents dans plus d'une playlist :")
message.pack()

message = tk.Label(app1bis, text="\nNombre d'artistes : \n dans 2 tops : "+str(c2)+"\n dans 3 tops : "+str(c3)+"\n dans 4 tops : "+str(c4)+"\n dans 5 tops : "+str(c5)+"\n dans 6 tops : "+str(c6)+"\n")
message.pack()

message = tk.Label(app1bis, text="Il est intéressant de voir ceux qui reviennent dans plus de 2 tops différents :")
message.pack()

n = len(top_total) #ensemble des tops d'un artiste
for i in range(n):
    if (len(top_total[i]) > 2): #si l'artiste apparait dans plus de 2 tops
        message = tk.Label(app1bis, text=str(dico_artistes[art[i]])+" est un artiste qui revient "+str(len(top_total[i]))+" fois.\n")
        message.pack()
        
#compte le nombre de fois qu'un duo de top contient le même artiste
compte = {}.fromkeys(set(top_total),0)
for valeur in top_total:
    compte[valeur] += 1

message = tk.Label(app1bis, text="Voici le nombre d'artistes qui reviennent pour chaque combinaison de tops existante : "+str(compte))
message.pack()

#combinaison de tops qui revient le plus 
import operator
max_key = max(compte.items(), key=operator.itemgetter(1))[0]

message = tk.Label(app1bis, text="\nLes décennies qui ont le plus d\'artistes en commun sont : "+str(max_key)+"\n")
message.pack()

#affichage des artistes qui sont dans la combinaison de top qui revient le plus
n = len(top_total)

message = tk.Label(app1bis, text="Artistes qui sont dans les tops "+str(max_key[0])+" et "+str(max_key[1])+" : ")
message.pack()

for p in range(n): #pour chaque combinaison
    if top_total[p]==max_key:
        message = tk.Label(app1bis, text=str(dico_artistes[art[p]]))
        message.pack()
  
    
#----------------Genres les plus populaires au fil des tops-------------------#
#Nous effectuons par la suite des analyses sur les genres musicaux

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app2, text="SUIVANT", bg="#9AE595", command=app2bis.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app2, text="PRECEDENT", bg="#F8DD96", command=app1bis.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app2, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#genres présents dans plusieurs tops
c = 0 #compteur genres
c2 = 0 #compteur genres 2 tops
c3 = 0 #compteur genres 3 tops
c4 = 0 #compteur genres 4 tops
c5 = 0 #compteur genres 5 tops
c6 = 0 #compteur genres 6 tops
top = list()
gen = list()
top_total = []
nrow = index_genres.shape[0] #nombre de lignes de la matrice d'index
ncol = index_genres.shape[1] #nombre de colonnes de la matrice d'index

message = tk.Label(app2, text="\nLa troisième étape est de voir quels sont les genres, cette fois-ci, qui reviennent dans plusieurs tops : ceux qui sont donc très populaires sur plus de dix ans : \n")
message.pack()

message = tk.Label(app2, text="Tous les genres qui reviennent dans plusieurs tops :")
message.pack()

for i in range(ncol): #pour chaque artiste
    for j in range (nrow): #pour chaque top
        if (index_genres[j][i] != 0): #si le genre est présent dans le top
            c += 1 #incrémentation du compteur
            nom_top = str(1950 + j * 10) #récupération du top
            top.append(int(nom_top)) #ajout du top à la liste
    if (c > 1): #si le genre apparait dans plusieurs tops
        gen.append(i) #ajout du genre à la liste
        #affichage des résultats dans l'interface
        message = tk.Label(app2, text=str(dico_genres[i])+" apparait dans "+str(c)+" tops : "+str(top)+".  ")
        message.pack()
        top_total.append(tuple(top)) #ajout des tops à la liste
        #incrémentations des compteurs en fonction de la présence du genre
        if (c == 2):
            c2 += 1
        elif(c == 3):
            c3 += 1
        elif (c == 4):
            c4 += 1
        elif (c == 5):
            c5 += 1
        else: 
            c6 += 1
        #le plus grand
        liste_c = (c, c2, c3, c4, c5, c6)
        max_c = max(liste_c)
        index = liste_c.index(max_c)
    #réinitialisation des variables
    c = 0
    top = list()
    
#bouton d'affichage de la fenêtre suivante
button = tk.Button(app2bis, text="SUIVANT", bg="#9AE595", command=app3.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app2bis, text="PRECEDENT", bg="#F8DD96", command=app2.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app2bis, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()
    
message = tk.Label(app2bis, text="\nNombre de genres : \n dans 2 tops : "+str(c2)+"\n dans 3 tops : "+str(c3)+"\n dans 4 tops : "+str(c4)+"\n dans 5 tops : "+str(c5)+"\n dans 6 tops : "+str(c6)+"\n")
message.pack()

message = tk.Label(app2bis, text=" => Nous pouvons voir que les genres reviennent le plus souvent dans "+str(index+1)+" tops.")
message.pack()

message = tk.Label(app2bis, text="\nIl peut être intéressant de voir ceux qui reviennent dans plus de 2 tops différents :")
message.pack()

n = len(top_total) #ensemble des tops d'un genre
for i in range(n):
    if (len(top_total[i]) > 2): #si le genre apparait dans plus de 2 tops
        message = tk.Label(app2bis, text=str(dico_genres[gen[i]])+" est un genre qui revient "+str(len(top_total[i]))+" fois.")
        message.pack()



#------------------Mots les plus populaires au fil des tops-------------------#
#Nous effectuons par la suite des analyses sur le vocabulaire utilisé entre les tops

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app3, text="SUIVANT", bg="#9AE595", command=app4.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app3, text="PRECEDENT", bg="#F8DD96", command=app2bis.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app3, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#mots présents dans plusieurs tops
c = 0 #compteur mots
c1 = 0 #compteur mots 1 tops
c2 = 0 #compteur mots 2 tops
c3 = 0 #compteur mots 3 tops
c4 = 0 #compteur mots 4 tops
c5 = 0 #compteur mots 5 tops
c6 = 0 #compteur mots 6 tops
top = list()
mot_top = list()
top_total = []
nrow = index_mots.shape[0] #nombre de lignes de la matrice d'index
ncol = index_mots.shape[1] #nombre de colonnes de la matrice d'index

message = tk.Label(app3, text="\n La quatrième étape est de voir quels sont les mots, cette fois-ci, qui reviennent dans plusieurs tops : ceux qui sont donc très populaires sur plus de dix ans : \n")
message.pack()

message = tk.Label(app3, text="Tous les mots qui reviennent dans plusieurs tops :")
message.pack()

for i in range(ncol): #pour chaque artiste
    for j in range (nrow): #pour chaque top
        if (index_mots[j][i] != 0): #si le mot est présent dans le top
            c += 1 #incrémentation du compteur
            nom_top = str(1950 + j * 10) #récupération du top
            top.append(int(nom_top)) #ajout du top à la liste
    if (c > 1): #si le mot apparait dans plusieurs tops
        mot_top.append(i) #ajout du mot à la liste
        #print(n_vocab[i]," apparait dans ",str(c)," tops : ",str(top),". ")  Trop de données pour l'afficher : 1300     
        top_total.append(tuple(top)) #ajout des tops à la liste
        #incrémentations des compteurs en fonction de la présence du mot
        if (c == 2):
            c2 += 1
        elif(c == 3):
            c3 += 1
        elif (c == 4):
            c4 += 1
        elif (c == 5):
            c5 += 1
        else: 
            c6 += 1
        #le plus grand:
        liste_c = (c, c2, c3, c4, c5, c6)
        max_c = max(liste_c)
        index = liste_c.index(max_c)
    else : c1+=1
    #réinitialisation des variables
    c = 0
    top = list()
    
message = tk.Label(app3, text="Nombre de mots : \n dans 1 top : "+str(c1)+"\n dans 2 tops : "+str(c2)+"\n dans 3 tops : "+str(c3)+"\n dans 4 tops : "+str(c4)+"\n dans 5 tops : "+str(c5)+"\n dans 6 tops : "+str(c6)+"\n")
message.pack()
message = tk.Label(app3, text="Nous notons logiquement que beaucoup de mots reviennent plusieurs fois, mais seulement une petite partie revient dans tous : on peut supposer surtout les mots-outils.")
message.pack()
 
n = len(top_total) #ensemble des tops d'un mot
count_mot = 0
for i in range(n):
    if ((len(top_total[i]) == 6 ) and len(n_vocab[mot_top[i]])>3): #si le mot apparait dans plus de 2 tops
        count_mot += 1
        #print(n_vocab[mot_top[i]]+" est un mot qui revient "+str(len(top_total[i]))+" fois.") Impossible à afficher, trop de données : 367

message = tk.Label(app3, text="Après avoir enlevé les mots de deux ou trois lettres, qui après rapide vérification sont souvent des verbes ou des mots outils, nous obtenons "+ str(count_mot)+" mots faisant partie des 6 tops, qui pourraient donc être dans des champs lexicaux de thèmes très populaires.")
message.pack()        


#-------------------------------Nuages de mots--------------------------------#
#Nous créons des nuages de mots afin d'afficher les données les plus présentes au sein des tops

#librairie de création des nuages de mots
from wordcloud import WordCloud

#fonction de récupération du nouveau vocabulaire en prenant en compte la fréquence de chaque mot
def freq_voc(frequences):
    voc = [] #liste des mots
    for mot in frequences: #pour chaque mot
        for i in range(frequences[mot]): #pour chaque apparition
           voc.append(mot) #ajout du mot
    return voc

#fonction de création du nuage de mots
def nuage(mots, fic):
    mots = ' '.join(mots) #ajout des mots dans une longue chaine de caractères
    wc = WordCloud(max_font_size=40, background_color="white").generate(mots) #création du nuage
    wc.to_file(fic) #récupération de l'image
    plt.imshow(wc, interpolation='bilinear') #méthode d'affichage
    plt.axis("off")
    plt.show() #affichage du nuage

#nuages de mots pour le vocabulaire global et de chaque top
f = freq_voc(fvocab)
voc = nuage(f, 'voc.png')
f = freq_voc(fvocab_1950)
voc_1950 = nuage(f, 'voc_1950.png')
f = freq_voc(fvocab_1960)
voc_1960 = nuage(f, 'voc_1960.png')
f = freq_voc(fvocab_1970)
voc_1970 = nuage(f, 'voc_1970.png')
f = freq_voc(fvocab_1980)
voc_1980 = nuage(f, 'voc_1980.png')
f = freq_voc(fvocab_1990)
voc_1990 = nuage(f, 'voc_1990.png')
f = freq_voc(fvocab_2000)
voc_2000 = nuage(f, 'voc_2000.png')

#nuages de mots pour les artistes de tous les tops et de chaque top
nuage_artistes = nuage(all_artistes, 'artistes.png')
nuage_artistes_1950 = nuage(artistes_1950, 'artistes_1950.png')
nuage_artistes_1960 = nuage(artistes_1960, 'artistes_1960.png')
nuage_artistes_1970 = nuage(artistes_1970, 'artistes_1970.png')
nuage_artistes_1980 = nuage(artistes_1980, 'artistes_1980.png')
nuage_artistes_1990 = nuage(artistes_1990, 'artistes_1990.png')
nuage_artistes_2000 = nuage(artistes_2000, 'artistes_2000.png')

#nuages de mots pour les genres de tous les tops et de chaque top
nuage_genres = nuage(all_genres, 'genres.png')
nuage_genres_1950 = nuage(genres_1950, 'genres_1950.png')
nuage_genres_1960 = nuage(genres_1960, 'genres_1960.png')
nuage_genres_1970 = nuage(genres_1970, 'genres_1970.png')
nuage_genres_1980 = nuage(genres_1980, 'genres_1980.png')
nuage_genres_1990 = nuage(genres_1990, 'genres_1990.png')
nuage_genres_2000 = nuage(genres_2000, 'genres_2000.png')
        
  
#Fenêtre d'affichage des nuages de mots du vocabulaire des tops 50, 60 et 70

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app4, text="SUIVANT", bg="#9AE595", command=app4bis.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app4, text="PRECEDENT", bg="#F8DD96", command=app3.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app4, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#ensemble stockant la référence des images
gifsdict={}

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app4, image=img) #attribution de l'image à la fenêtre app4
    image.pack() #ajout de l'image

message = tk.Label(app4, text="Nuage de mots du vocabulaire du top 1950 :")
message.pack()
affiche_image('voc_1950.png') #appel de la fonction affiche_image()
message = tk.Label(app4, text="Nuage de mots du vocabulaire du top 1960 :")
message.pack()
affiche_image('voc_1960.png') #appel de la fonction affiche_image()
message = tk.Label(app4, text="Nuage de mots du vocabulaire du top 1970 :")
message.pack()
affiche_image('voc_1970.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots du vocabulaire des tops 80, 90 et 00

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app4bis, text="SUIVANT", bg="#9AE595", command=app5.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app4bis, text="PRECEDENT", bg="#F8DD96", command=app4.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app4bis, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app4bis, image=img) #attribution de l'image à la fenêtre app4bis
    image.pack() #ajout de l'image

message = tk.Label(app4bis, text="Nuage de mots du vocabulaire du top 1980 :")
message.pack()
affiche_image('voc_1980.png') #appel de la fonction affiche_image()
message = tk.Label(app4bis, text="Nuage de mots du vocabulaire du top 1990 :")
message.pack()
affiche_image('voc_1990.png') #appel de la fonction affiche_image()
message = tk.Label(app4bis, text="Nuage de mots du vocabulaire du top 2000 :")
message.pack()
affiche_image('voc_2000.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots des artistes des tops 50, 60 et 70

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app5, text="SUIVANT", bg="#9AE595", command=app5bis.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app5, text="PRECEDENT", bg="#F8DD96", command=app4bis.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app5, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app5, image=img) #attribution de l'image à la fenêtre app5
    image.pack() #ajout de l'image

message = tk.Label(app5, text="Nuage de mots des artistes du top 1950 :")
message.pack()
affiche_image('artistes_1950.png') #appel de la fonction affiche_image()
message = tk.Label(app5, text="Nuage de mots des artistes du top 1960 :")
message.pack()
affiche_image('artistes_1960.png') #appel de la fonction affiche_image()
message = tk.Label(app5, text="Nuage de mots des artistes du top 1970 :")
message.pack()
affiche_image('artistes_1970.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots des artistes des tops 80, 90 et 00

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app5bis, text="SUIVANT", bg="#9AE595", command=app6.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app5bis, text="PRECEDENT", bg="#F8DD96", command=app5.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app5bis, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app5bis, image=img) #attribution de l'image à la fenêtre app4bis
    image.pack() #ajout de l'image

message = tk.Label(app5bis, text="Nuage de mots des artistes du top 1980 :")
message.pack()
affiche_image('artistes_1980.png') #appel de la fonction affiche_image()
message = tk.Label(app5bis, text="Nuage de mots des artistes du top 1990 :")
message.pack()
affiche_image('artistes_1990.png') #appel de la fonction affiche_image()
message = tk.Label(app5bis, text="Nuage de mots des artistes du top 2000 :")
message.pack()
affiche_image('artistes_2000.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots des genres des tops 50, 60 et 70

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app6, text="SUIVANT", bg="#9AE595", command=app6bis.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app6, text="PRECEDENT", bg="#F8DD96", command=app5bis.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app6, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app6, image=img) #attribution de l'image à la fenêtre app6
    image.pack() #ajout de l'image

message = tk.Label(app6, text="Nuage de mots des genres du top 1950 :")
message.pack()
affiche_image('genres_1950.png') #appel de la fonction affiche_image()
message = tk.Label(app6, text="Nuage de mots des genres du top 1960 :")
message.pack()
affiche_image('genres_1960.png') #appel de la fonction affiche_image()
message = tk.Label(app6, text="Nuage de mots des genres du top 1970 :")
message.pack()
affiche_image('genres_1970.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots des genres des tops 80, 90 et 00

#bouton d'affichage de la fenêtre suivante
button = tk.Button(app6bis, text="SUIVANT", bg="#9AE595", command=app7.lift)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app6bis, text="PRECEDENT", bg="#F8DD96", command=app6.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app6bis, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app6bis, image=img) #attribution de l'image à la fenêtre app6bis
    image.pack() #ajout de l'image

message = tk.Label(app6bis, text="Nuage de mots des genres du top 1980 :")
message.pack()
affiche_image('genres_1980.png') #appel de la fonction affiche_image()
message = tk.Label(app6bis, text="Nuage de mots des genres du top 1990 :")
message.pack()
affiche_image('genres_1990.png') #appel de la fonction affiche_image()
message = tk.Label(app6bis, text="Nuage de mots des genres du top 2000 :")
message.pack()
affiche_image('genres_2000.png') #appel de la fonction affiche_image()


#Fenêtre d'affichage des nuages de mots globaux

#bouton de fermeture de l'interface
button = tk.Button(app7, text="FERMER", bg="#F38070", command=root.destroy)
button.pack()
#bouton d'affichage de la fenêtre précédente
button = tk.Button(app7, text="PRECEDENT", bg="#F8DD96", command=app6bis.lift)
button.pack()
#bouton d'affichage de la fenêtre accueil
button = tk.Button(app7, text="ACCUEIL", bg="#ADDEEF", command=root.lift)
button.pack()

message = tk.Label(app7, text="Voici les nuages de mots représentant les mots, artistes et genres les plus présents dans nos répertoires.\n")
message.configure(font="bold")
message.pack()

#fonction d'affichage des nuages de mots dans l'interface
def affiche_image(fic):
    img = tk.PhotoImage(file=fic) #création d'un objet image
    gifsdict[fic]=img  #stockage de l'objet
    image = tk.Label(app7, image=img) #attribution de l'image à la fenêtre app7
    image.pack() #ajout de l'image

message = tk.Label(app7, text="Nuage de mots du vocabulaire de l'ensemble des tops :")
message.pack()
affiche_image('voc.png') #appel de la fonction affiche_image() pour le vocabulaire global
message = tk.Label(app7, text="Nuage de mots des artistes de l'ensemble des tops :")
message.pack()
affiche_image('artistes.png') #appel de la fonction affiche_image() pour les artistes
message = tk.Label(app7, text="Nuage de mots des genres de l'ensemble des tops :")
message.pack()
affiche_image('genres.png') #appel de la fonction affiche_image() pour les genres musicaux

#affichage de l'interface
root.mainloop()