#-----------------------------------CLASSES-----------------------------------#
class Musique:
    #constructeur
    #initialisation des attributs de la classe
    def __init__(self, titre="", album="", artiste="", genre="", date="", duree="", top=""):
        self.titre = titre #titre de la chanson
        self.album = album #nom de l'album
        self.artiste = artiste #nom de l'artiste
        self.genre = genre #genres musicaux de l'artiste
        self.date = date #date de sortie
        self.duree = duree #durée de la chanson
        self.top = top #top dans lequel se trouve la chanson

    #méthodes d'affichage
    def __repr__(self):
        return f"Top : {self.top}\tTitre : {self.titre}\tAlbum : {self.album}\tArtiste : {self.artiste}\tDate : {self.date}\tDurée : {self.duree}\t"

    def __str__(self):
        return f"{self.titre}, par {self.artiste}"
    
    
class Artiste:
    #constructeur
    #initialisation des attributs de la classe
    def __init__(self, artiste, genre):
        self.artiste = artiste #nom de l'artiste
        self.genre = genre #genres musicaux de l'artiste
        self.repertoire = [] #répertoire musical de l'artiste présent dans les différents tops

    #méthode d'ajout
    def add(self, musique):
        self.repertoire.append(musique) #ajout d'une chanson au répertoire de l'artiste
        
    #méthodes d'affichage
    def __repr__(self):
        return f"Artiste : {self.artiste}\tGenres Musicaux : {self.genre}\tRepertoire : {self.repertoire}"

    def __str__(self):
        return f"Repertoire : {self.repertoire}, par {self.artiste}"


#----------------------------------HERITAGE-----------------------------------#
class MusiqueAvecParoles(Musique):
    #constructeur
    #initialisation des attributs de la classe
    def __init__(self, titre="", album="", artiste="", genre="", date="", duree="", top="", paroles=""): 
        super().__init__(titre=titre, album=album, artiste=artiste, genre=genre, date=date, duree=duree, top=top) #attributs de la classe-mère
        self.paroles = paroles #paroles de la chanson
        
    #accesseur
    def get_paroles(self):
        return self.paroles

    #mutateur
    def set_paroles(self, paroles):
        self.paroles = paroles

    #méthodes d'affichage
    def __repr__(self):
        return f"Titre : {self.titre}\tArtiste : {self.artiste}\tParoles : {self.paroles}\t"

    def __str__(self):
        return f"{self.titre}, par {self.artiste} : {self.paroles}"