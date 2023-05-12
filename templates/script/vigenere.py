<<<<<<< HEAD
def vigenere_encode(message, key):
    encoded_message = ""
    key_index = 0
    
    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            # Convertit la lettre en majuscule pour faciliter le chiffrement
            char = char.upper()
            
            # Calcule le décalage correspondant à la lettre de la clé
            shift = ord(key[key_index].upper()) - ord('A')
            
            # Applique le décalage à la lettre du message
            encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
            key_index = (key_index + 1) % len(key)  # Passe à la lettre suivante de la clé
        else:
            encoded_char = char  # Conserve les caractères non alphabétiques inchangés
        
        encoded_message += encoded_char
    
    return encoded_message
=======
dico =  {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13, 'o': 14,'p': 15,'q':16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25}
tab = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
       ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'],
       ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b'],
       ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c'],
       ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],
       ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e'],
       ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f'],
       ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g'],
       ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h'],
       ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i'],
       ['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j'],
       ['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k'],
       ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l'],
       ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m'],
       ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n'],
       ['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'],
       ['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'],
       ['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'],
       ['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'],
       ['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],
       ['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'],
       ['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],
       ['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'],
       ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'],
       ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'],
       ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']]

def vigenere_encode(phrase):
    code = ""
    liste_cle, cle, l_ph, carac = [], [], [], [] 
    cle = list(cle_code)
    l_ph = list(phrase)
    x = 0
    for i in range(len(l_ph)):
        if l_ph[i] == " ": 
            liste_cle.append(" ")
        else:
            if x >= len(cle):
                x = 0
            liste_cle.append(cle[x])
            x += 1
    for j in range(len(liste_cle)):
        for ele in dico.items():
            if liste_cle[j] == ele[0]:
                val_cle = ele[1]
    for h in range(len(l_ph)):
        if l_ph[h] == ' ':
                carac.append(" ")
        for ele in dico.items():
            if l_ph[h] == ele[0]:
                val = ele[1]
                carac.append(tab[val][val_cle])
    for g  in carac:
        code = code + g
    return code

def boom(code):
    chiffre_cle_trouver = 0
    phrase_deco = ""
    tab_fin = []
    ph_decode = []
    x = 0
    cle = list(cle_code)
    split_code = list(code)
    for lettre_code in range(len(split_code)):
        for chiffre_cle in dico.items():
            if x< len(cle):
                x = 0
                if chiffre_cle == cle[x]:
                    chiffre_cle_trouver = chiffre_cle
        
        if x< len(cle):
            tab_fin.append(tab[lettre_code][chiffre_cle_trouver])
        else:
            x = 0
            tab_fin.append(tab[lettre_code][chiffre_cle_trouver])
        x += 1
    for lettre in tab_fin:
        for ele in dico.items():
            if lettre == ele[1]:
                ph_decode.append(ele[0])
            elif lettre ==' ':
                ph_decode.append(" ")
    for p in ph_decode :
        phrase_deco = phrase_deco + p
    return phrase
<<<<<<< HEAD
>>>>>>> 2c1d528fa2ef8fbc874f1c7acdd7aa75714dd327
=======
>>>>>>> 2c1d528fa2ef8fbc874f1c7acdd7aa75714dd327


def vigenere_decode(encoded_message, key):
    decoded_message = ""
    key_index = 0
    
    for char in encoded_message:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decoded_char = char
        
        decoded_message += decoded_char
    
    return decoded_message


# Exemple d'utilisation :
message = "test si ' ' ' ca marche pour le francais"
key = "l'aluminium"

encoded_message = vigenere_encode(message, key)
print("Message encodé:", encoded_message)

decoded_message = vigenere_decode(encoded_message, key)
print("Message décodé:", decoded_message)
