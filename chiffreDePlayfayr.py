import pygame
from pygame import *

def remplacementW(chaine):
#on parcourt la chaine à la recherche de 'W' qu'on remplace par des 'v' et on retourne la chaine
    for car in chaine:
        if car =='w' or car == 'W':
            chaine = chaine.replace(car,"v")
    return chaine

def ajoutXbi(chaine):
#on parcourt la chaine sur tout sa longueur, si on détecte 2caractères identique à la suite, on ajoute un 'X' entre
#les deux et on retourne la chaine
    for i in range(0, len(chaine)):
        if chaine[i] == chaine[i-1]:
            chaine = chaine[:i] + 'X' + chaine[i:]
    return chaine


def ajoutXFin(chaine):
#On parcout chaque caractère de la chaine et on regarde si ce n'est pas un espace. En effet len(chaine) retourne la
#longueur de la chaine, en comptant les espaces. Or on ne veut compter que les caractères.
#Une autre méthode aurait été de faire un compteur qui compte uniquement les caractères.
    longueur = 0
    for car in chaine:
        if car == ' ':
            longueur = longueur + 1
    longueur = len(chaine) - longueur
    if longueur%2 > 0:
        chaine = chaine +'X'
    return chaine

def carré(cle):
#On passe la clé en majuscule, on crée un tableau à deux dimensions de 5lignes et 5colonnes auquelle on atribue les
#caractères de la clé un par un. Ensuite on l'affiche sous la forme d'un carré et on le retourne.
    cle = cle.upper()
    carré = [[0] *5 for i in range(5)]
    a = 0
    for j in range(0, len(carré)):
        for y in range(0, len(carré[j])):
            carré[j][y] = cle[a]
            a += 1
    for ligne in carré:
        for x in ligne:
            print(x, ' ', end='')
        print('\n')
    return carré

def indice(plateau, caractere):
#J parcourt les lignes, y les colonnes. Si on trouve le caractère donné en paramètre dans le plateau, on retourne
#ses coordonnées dans le plateau.
   for j in range(0, len(plateau)):
        for y in range(0, len(plateau)):
            if plateau[j][y] == caractere:
                return j, y

def codage(j1, y1, j2, y2):
#Cette fonction modifie les coordonnées des caractères données en paramètres pour les coder. J1 et Y1 correspondent au
#caractère 1 et J2 et Y2 au second caractère.
    if j1 == j2:
#Cas où les deux caractères sont sur la même ligne. Si un des deux caractères est sur la dernière colonne, après le codage
#il sera sur la première colonne (soit la colonne 0 en python). On aurait pu mettre y1 = 0, mais le modulo marche
#également et permet de réutiliser le cours de mathématique
        if y1 == 4:
            y1 = y1%4
            y2 = y2 +1
        elif y2 == 4:
            y1 = y1 +1
            y2 = y2 %4
        else:
#si aucun des caractères n'est sur la dernière colonne, on ajoute juste une colonne
            y1 = y1 + 1
            y2 = y2 + 1
    elif y1 == y2:
#Meme principe que précédemment appliqué aux lignes
       if j1 == 4:
            j1 = j1%4
            j2 = j2+1
       elif j2 == 4:
           j1 = j1 +1
           j2 = j2%4
       else:
            j1 = j1 +1
            j2 = j2 + 1
    else:
#Si les deux caractères ne sont pas sur la même ligne ou la même colonne, on inverse les Y des deux caractères pour
#obtenir les coordonnées des caractères des autres coins du rectangle
        c = y1
        y1 = y2
        y2 = c
    return j1, y1, j2, y2


def chiffrementBigramme(caractere1, caractere2, plateau):
#Pour chiffrer le bigramme, on va chercher les coordonnées des caractères passés en paramètres avec la fonction
#indice(), ensuite on va coder ces 4 coordonnées avec la fonction codage(). Les deux caractères codés sont donc
#les caractères correspondant aux nouvelles coordonnées obtenus. On a juste à les rentrer dans la clé pour savoir
#de quel caractère il s'agit. On retourne le bigramme chiffré ainsi obtenu.
    j1,y1 = indice(plateau, caractere1)
    j2,y2 = indice(plateau, caractere2)
    j1,y1,j2,y2 = codage(j1,y1,j2,y2)
    caractere1 = plateau[j1][y1]
    caractere2 = plateau[j2][y2]
    return caractere1, caractere2

def chiffrementTexte(texte, clé):
#On initie une chaine de caractère vide. Ensuite on applique les fonctions de modifications de chaine au texte (on
#change de les W etc..). Ensuite on parcout la chaine et on remplace les espaces par un vide (concrétement l'espace
#est supprimé). Ensuite on initie le compteur i, qui parcourt la chaine et envoie tous les caractères du texte dans
#la fonction chiffrementBigramme qui chiffre tous les bigrammes. On affiche le texte chiffré intégralement à la fin.
    textechiffre = ""
    texte = remplacementW(texte)
    texte = ajoutXbi(texte)
    texte = ajoutXFin(texte)
    i = 0
    for car in texte:
        if car == ' ':
            texte = texte.replace(car, '')
    while i < len(texte)-1:
        caractere1, caractere2 = chiffrementBigramme(texte[i], texte[i+1], clé)
        textechiffre = textechiffre + caractere1 + caractere2
        i = i + 2
    print(textechiffre)
    chiffre = textechiffre
    return chiffre

def decodage(j1, y1, j2, y2):
#Cette fonction est juste une modification de la fonction codage. Cncrètement elle fait l'inverse de la fonction
#codage
    if j1 == j2:
        if y1 == 0:
            y1 = 4
            y2 = y2 - 1
        elif y2 == 0:
            y1 = y1 -1
            y2 = 4
        else:
            y1 = y1 - 1
            y2 = y2 - 1
    elif y1 == y2:
       if j1 == 0:
            j1 = 4
            j2 = j2 - 1
       elif j2 == 0:
           j1 = j1 - 1
           j2 = 4
       else:
            j1 = j1 - 1
            j2 = j2 - 1
    else:
        c = y1
        y1 = y2
        y2 = c
    return j1, y1, j2, y2

def dechiffrementBigramme(caractere1, caractere2, plateau):
#Il s'agit ici également de la même fonction que chiffrementBigramme(), on a juste remplacé codage() par decodage()
    j1,y1 = indice(plateau, caractere1)
    j2,y2 = indice(plateau, caractere2)
    j1,y1,j2,y2 = decodage(j1,y1,j2,y2)
    caractere1 = plateau[j1][y1]
    caractere2 = plateau[j2][y2]
    return caractere1, caractere2


def dechiffrementTexte(texte, clé):
#comme les deux fonctions présentes, cette fonction n'est qu'une version modifié de la focntion chiffrementTexte, on
#a juste changé le nom de quelques variables et fonctions.
    texteDechiffre = ""
    i = 0
    for car in texte:
        if car == ' ':
            texte = texte.replace(car, '')
    while i < len(texte)-1:
        caractere1, caractere2 = dechiffrementBigramme(texte[i], texte[i+1], plateau)
        texteDechiffre = texteDechiffre + caractere1
        texteDechiffre = texteDechiffre + caractere2
        i = i + 2
    print(texteDechiffre)


def cleGUI():
#Ceci est la fonction qui permet de saisir la clé avec une interface graphique
    alphabet = "abcdefghijklmnopqrstuvxyz"
    alphabet = alphabet.upper()
    marron = (61, 43, 31)
    jaune = (133, 83, 15)
    carré = [[0] *5 for o in range(5)]
    i = 0
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((jaune))
    fontObj = pygame.font.Font(None, 60)
    text = fontObj.render("Positionner la lettre :", 1, marron)
    pygame.draw.line(background,marron,(100, 100),(100,600),5)
    pygame.draw.line(background,marron,(200, 100),(200,600),5)
    pygame.draw.line(background,marron,(300, 100),(300,600),5)
    pygame.draw.line(background,marron,(400, 100),(400,600),5)
    pygame.draw.line(background,marron,(500, 100),(500,600),5)
    pygame.draw.line(background,marron,(600, 100),(600,600),5)
    pygame.draw.line(background,marron,(100, 100),(600,100),5)
    pygame.draw.line(background,marron,(100, 200),(600,200),5)
    pygame.draw.line(background,marron,(100, 300),(600,300),5)
    pygame.draw.line(background,marron,(100, 400),(600,400),5)
    pygame.draw.line(background,marron,(100, 500),(600,500),5)
    pygame.draw.line(background,marron,(100, 600),(600,600),5)
    background.blit(text, (750,200))
    screen.blit(background, (0,0))
    pygame.display.flip()
    dimX, dimY = 100, 100
    inProgress = True
    while inProgress:
        pygame.draw.rect(background,(jaune), (800, 250 ,300, 200), 0)
        fontObj = pygame.font.Font(None, 200)
        textLettre = fontObj.render(alphabet[i], 1, marron)
        background.blit(textLettre, (900,300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                InProgress = False
            elif event.type == MOUSEBUTTONDOWN:
                posSouris = pygame.mouse.get_pos()
                posCaseX = (posSouris[0]) // dimX
                posCaseY = (posSouris[1]) // dimY
                if  0 < posCaseX < 6 and 0 < posCaseY < 6 and i < 25:
                    if carré[posCaseX-1][posCaseY-1] == 0:
                        fontObj = pygame.font.Font(None, 100)
                        textLoop = fontObj.render(alphabet[i], 1, marron)
                        carré[posCaseX-1][posCaseY-1] = alphabet[i]
                        i += 1
                        background.blit(textLoop,(posCaseX*100+25, posCaseY*100+25))
                if i == 25:
                    inProgress = False
                    return carré
        screen.blit(background, (0,0))
        pygame.display.flip()


#Pour modifier une clé, merci de bien vouloir modifier la ligne : cle = open(fichier, "r") où fichier est le
#fichier que vous désirez comme clé. Par défaut il s'agit de la clé donné avec l'énoncé.
#Si vous désirez utilisé l'interface graphique pour faire votre clé, merci de mettre tout en commentaire, sauf
#cle = cleGUI()

fichierCle = "clePf.txt"
fichierCleEleve = "clePfEleve.txt"
cle = open(fichierCle, "r")
cle = cle.read()
plateau = carré(cle)
cle = cleGUI()

#Pour modifier un chiffre, merci de bien vouloir modifier la ligne : cle = open(fichier, "r") où fichier est le
#fichier que vous désirez comme chiffre. Par défaut il s'agit du chiffre donné avec l'énoncé.

fichierChiffre = "chiffrePf.txt"
fichierChiffreEleve = "chiffrePfEleve.txt"
chiffre = open(fichierChiffre, 'r')
chiffre = chiffre.read()
dechiffrementTexte(chiffre, cle)


