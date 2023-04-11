
#-------------------------------------------------------------#
# Méthode de recherche naïve (ou brute force)
#-------------------------------------------------------------#
#   Entrées :
#       - Chaine de caractère (texte)
#       - Motif à rechercher (clé)
#
#   Sortie :
#       - Listes des occurences de la clé dans la phrase
#-------------------------------------------------------------#
def naive(texte, cle):

    long_txt = len(texte)
    long_cle = len(cle)
    positions = []
    i=0 #position du motif
    trouve = False
    while (i .............................): #on parcourt toute la chaine jusqu'a la derniere position possible
        for j in range (......................): #on parcourt toutes les lettres du motif
            trouve = True

            if .......................... :
                trouve = False
                break

        if trouve :
            positions.append(...............)
        i+=1
    return positions


#-------------------------------------------------------------#
# Détermination de la "table de sauts" pour l'algorithme de Boyer Moore
#-------------------------------------------------------------#
#   Entrée :
#       - Motif à rechercher
#
#   Sortie :
#       - Dictionnaire des sauts en fonction du motif
#-------------------------------------------------------------#
def table_sauts(mot):

    sauts=







    return sauts


#-------------------------------------------------------------#
# Méthode de recherche de Boyer-Moore
#-------------------------------------------------------------#
#   Entrées :
#       - Chaine de caractère (texte)
#       - Motif à rechercher (clé)
#
#   Sortie :
#       - Listes des occurences de la clé dans la phrase
#-------------------------------------------------------------#
def boyer_moore (texte, cle):

    long_txt = ..................
    long_cle = ..........................
    positions = []
    if long_cle <= long_txt :
        decalage = table_sauts(cle) #on détermine le dictionnaire des décalages
        i=0
        trouve = False
        while (i .........................): #on parcourt toute la chaine jusqu'a la derniere position possible
            for j in range (.................................): #on parcourt toutes les lettres du motif mais de la droite vers la gauche
                trouve = ...................

                if ............................ :
                    trouve = .................
                    break

            if trouve :
                positions.append(................)
            if (texte[i+long_cle-1] in .....................): # si le décalage existe dans le dictionnaire
                .......................................... # alors on applique ce décalage
            else:
                ............................ # sinon on applique un décalage maximum

    return positions


####################################################################
####################################################################
####                   PROGRAMME PRINCIPAL                      ####
####################################################################
####################################################################

#-------------------------------------------------------------#
# Création de la chaine de caractère
#-------------------------------------------------------------#

phrase= "ACCAAGATTCCGGAGGTCCTTA" #['A','C','C','A','A','G','A','T','T','C',' C','G','G','A','G','G','T','C','C','T','T','A']


#-------------------------------------------------------------#
# Création du motif
#-------------------------------------------------------------#
motif= "AGGTC" #['A','G','G','T','C']

#-------------------------------------------------------------#
#  Execution des algorithmes de recherche textuelle
#  Affichage pour chaque algorithme :
#       - de la position des occurences trouvées,
#       - du temps d'exécution,
#       - du nombre d'occurences trouvée.
#-------------------------------------------------------------#

# à compléter