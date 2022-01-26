# -*- coding: utf-8 -*-
#--------------------------------CONNEXION APIs-------------------------------#
#Nous nous connectons ici aux APIs Spotipy et Genius afin de pouvoir récupérer les playlists et leurs paroles

#modules
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from lyricsgenius import Genius

#identifiants Spotify
client_id ='4b39b4f6af9b4d3391c149dfddd1d406'
client_secret = '3950f4bb43d74133a2d3ac9d1deefe22'
username = 'ProjetAlgo'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #connexion Spotipy
genius = Genius('xtyqsbmj09rm0CY1QGn1hpENy5ljCUz09Ox16ThFds94WA9zANuOzfGnXh8PdVxZ') #connexion Genius
genius.remove_section_headers = True #paramètre supprimant les informations complémentaires dans les paroles récupérées


#---------------------------------FONCTIONS-----------------------------------#
#Nous retrouvons l'ensemble des fonctions nécessaires à la récupération des données

print("Connexions aux APIs de Spotify et Genius...\n")

#fonction de récupération des id des musiques d'une playlist
def getTrackID(user,playlist_id):
    id = [] #initialisation de la liste des identifiants
    play_list = sp.user_playlist(user,playlist_id) #récupération des informations d'une playlist
    for item in play_list['tracks']['items']: #pour chaque item de la playlist
        track = item['track'] 
        id.append(track['id']) #ajout des identifiants dans la liste
    return id

#module
import re

#fonction de récupération des informations d'une musique
def getTrackFeatures(id):
    meta = sp.track(id) #récupération de toutes les informations d'une musique
    name = meta['name'] #nom du titre
    #expressions régulières prenant les informations complémentaires contenues dans les titres (version, theme, edit, feat, remasterisation) 
    regex = '( - [A-Za-z0-9\.,\"\'\[\] ]+)|(-[A-Za-z0-9\.,\"\'\[\] ]+)|(; [A-Za-z0-9\.,\"\' ]+)'       
    regex2 = '( \([A-Za-z0-9\.,\"\'\[\]& ]+\))|(/[A-Za-z0-9\.,\"\'\[\] ]+)|( \[[A-Za-z0-9\.,\"\' ]+\])'
    name = re.sub(regex, '', name) #suppression de l'expression régulière 1 du titre si existant
    name = re.sub(regex2, '', name) #suppression de l'expression régulière 2 du titre si existant
    album = meta['album']['name'] #nom de l'album
    artist = meta['album']['artists'][0]['name'] #nom de l'artiste
    result = sp.search(artist) #recherche de l'artiste
    track = result['tracks']['items'][0] #récupération des informations musicales
    artiste = sp.artist(track["artists"][0]["external_urls"]["spotify"]) #récupération des informations musicales
    genre = artiste["genres"] #genres musicaux de l'artiste
    date = meta['album']['release_date'] #date de sortie
    duree = meta['duration_ms'] #durée
    duree = duree/60000 #conversion de la durée en minutes
    track = [name, album, artist, genre, date, duree] #stockage des variables dans une liste à retourner
    return track 

#fonction de récupération des musiques d'un top
def getTrack(id):
    tracks = [] #initialisation de la liste des musiques
    for i in range(len(id)): #pour chaque identifiant de musique
        res = getTrackFeatures(id[i]) #récupération des informations de la musique
        tracks.append(res) #ajout des informations dans la liste
    return tracks
        
#fonction de récupération des paroles d'une musique
def getLyrics(chanson,artiste):
    genius.timeout = 15 #initialisation du timeout de l'API
    genius.sleep_time = 30 #initialisation du sleep time de l'API
    chanson = chanson #récupération du titre
    artiste = artiste #récupération de l'artiste
    song = genius.search_song(chanson, artiste) #appel de l'API pour rechercher les paroles de la musique
    if (type(song) != type(None)): #si les paroles de la musique ont été trouvées
        song.lyrics = song.lyrics.replace("\n", " ") #suppression des sauts de ligne
        return song.lyrics
    else:
        return None
   
#fonction de récupération des paroles d'une playlist
def getAllLyrics(data):
    paroles = [] #initialisation de la liste des paroles
    for i in range(len(data)): #pour chaque musique de la playlist
        chanson = data[i][0] #récupération du titre
        artiste = data[i][2] #récupération de l'artiste
        if (artiste == 'Various Artists'): #si l'artiste de la musique n'est pas renseigné.e, itération suivante 
            continue
        res = getLyrics(chanson,artiste) #récupération des paroles de la musique
        lyrics = [chanson,artiste,res] #stockage du titre, de l'artiste et des paroles dans une liste
        if (res != None): #si les paroles ont été trouvées
            paroles.append(lyrics) #ajout des informations dans la liste
    return paroles


#récupération des identifiants des musiques dans les playlists Spotify de chaque top
id_2000 = getTrackID('cac070796efd4d24','37i9dQZF1DX4o1oenSJRJd') #identifiant de la playlist Spotify "All Out 2000s" https://open.spotify.com/playlist/37i9dQZF1DX4o1oenSJRJd
id_1990 = getTrackID('cac070796efd4d24','37i9dQZF1DXbTxeAdrVG2l') #identifiant de la playlist Spotify "All Out 90s" https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l
id_1980 = getTrackID('cac070796efd4d24','37i9dQZF1DX4UtSsGT1Sbe') #identifiant de la playlist Spotify "All Out 80s" https://open.spotify.com/playlist/37i9dQZF1DX4UtSsGT1Sbe
id_1970 = getTrackID('cac070796efd4d24','37i9dQZF1DWTJ7xPn4vNaz') #identifiant de la playlist Spotify "All Out 70s" https://open.spotify.com/playlist/37i9dQZF1DWTJ7xPn4vNaz
id_1960 = getTrackID('cac070796efd4d24','37i9dQZF1DXaKIA8E7WcJj') #identifiant de la playlist Spotify "All Out 60s" https://open.spotify.com/playlist/37i9dQZF1DXaKIA8E7WcJj
id_1950 = getTrackID('cac070796efd4d24','37i9dQZF1DWSV3Tk4GO2fq') #identifiant de la playlist Spotify "All Out 50s" https://open.spotify.com/playlist/37i9dQZF1DWSV3Tk4GO2fq


#--------------------------------MUSIQUES-------------------------------------#
#Nous récupèrons les chansons des playlists de chaque top choisi en appelant la fonction getTrack()

print("Recuperation des chansons des playlists selectionnees... \n")

#MUSIQUES ANNEES 2000
tracks_2000 = getTrack(id_2000)

#MUSIQUES ANNEES 1990
tracks_1990 = getTrack(id_1990)

#MUSIQUES ANNEES 1980
tracks_1980 = getTrack(id_1980)

#MUSIQUES ANNEES 1970
tracks_1970 = getTrack(id_1970)

#MUSIQUES ANNEES 1960
tracks_1960 = getTrack(id_1960)

#MUSIQUES ANNEES 1950
tracks_1950 = getTrack(id_1950)


#En raison du temps important que prend la récupération des paroles, nous avons fait le choix
#de les récupérer ultérieurement et de les stocker dans des fichiers CSV, pour ensuite les récupérer facilement.
'''
#----------------------------------PAROLES------------------------------------#
#PAROLES ANNEES 2000
lyrics_2000 = getAllLyrics(tracks_2000)
#création du fichier csv
ly_2000 = pd.DataFrame(lyrics_2000)
ly_2000.to_csv('lyrics_2000.csv',sep=';')

#PAROLES ANNEES 1990
lyrics_1990 = getAllLyrics(tracks_1990)
#création du fichier csv
ly_1990 = pd.DataFrame(lyrics_1990)
ly_1990.to_csv('lyrics_1990.csv',sep=';')

#PAROLES ANNEES 1980
lyrics_1980 = getAllLyrics(tracks_1980)
#création du fichier csv
ly_1980 = pd.DataFrame(lyrics_1980)
ly_1980.to_csv('lyrics_1980.csv',sep=';')

#PAROLES ANNEES 1970
lyrics_1970 = getAllLyrics(tracks_1970)
#création du fichier csv
ly_1970 = pd.DataFrame(lyrics_1970)
ly_1970.to_csv('lyrics_1970.csv',sep=';')

#PAROLES ANNEES 1960
lyrics_1960 = getAllLyrics(tracks_1960)
#création du fichier csv
ly_1960 = pd.DataFrame(lyrics_1960)
ly_1960.to_csv('lyrics_1960.csv',sep=';')

#PAROLES ANNEES 1950
lyrics_1950 = getAllLyrics(tracks_1950)
#création du fichier csv
ly_1950 = pd.DataFrame(lyrics_1950)
ly_1950.to_csv('lyrics_1950.csv',sep=';')
'''

#-----------------------RECUPERATION DES PAROLES------------------------------#
#Nous récupèrons les paroles des chansons stockées juste avant dans des fichiers CSV

#module
import pandas as pd 

print("Recuperation des paroles... \n")

#PAROLES ANNEES 2000
lyrics_2000 = pd.read_csv("lyrics_2000.csv", sep=";", header=None)

#PAROLES ANNEES 1990
lyrics_1990 = pd.read_csv("lyrics_1990.csv", sep=";", header=None)

#PAROLES ANNEES 1980
lyrics_1980 = pd.read_csv("lyrics_1980.csv", sep=";", header=None)

#PAROLES ANNEES 1970
lyrics_1970 = pd.read_csv("lyrics_1970.csv", sep=";", header=None)

#PAROLES ANNEES 1960
lyrics_1960 = pd.read_csv("lyrics_1960.csv", sep=";", header=None)

#PAROLES ANNEES 1950
lyrics_1950 = pd.read_csv("lyrics_1950.csv", sep=";", header=None)