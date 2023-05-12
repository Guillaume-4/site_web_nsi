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
    for k in cle_code:
        cle.append(k)
    for b in phrase:
        l_ph.append(b)     
    print(l_ph)   
    print(cle)
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

def boom(message_chiffre, cle):
    message_dechiffre = ""
    i = 0
    for lettre in message_chiffre:
        # Si la lettre n'est pas une lettre de l'alphabet, on la laisse inchangée
        if lettre not in dico:
            message_dechiffre += lettre
            continue
        # On décale la lettre de la clé correspondante
        decalage = dico[cle[i % len(cle)]]
        lettre_dechiffre = tab[dico[lettre]][decalage]
        # On ajoute la lettre déchiffrée au message déchiffré
        
        message_dechiffre += lettre_dechiffre
        i += 1
    return message_dechiffre



phrase = "test si c bon et ouais ma guele"
cle_code = 'vroum'
ph_code = vigenere_encode(phrase)
print(ph_code)
print(boom(ph_code, cle_code))
