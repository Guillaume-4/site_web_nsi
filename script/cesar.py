dico_alpha = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14, 'o': 15,'p': 16,'q':17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}

def coder(phrase):
    phrase_terminer = ""
    phrase_code = []
    for i in range(len(phrase)):
        for ele in dico_alpha.items():
            if phrase[i] == ele[0]:
                v = ele[1] + x
        for ele in dico_alpha.items():
            if v == ele[1]:
                phrase_code.append(ele[0])
    print(phrase_code)
    for j in phrase_code:
        phrase_terminer = phrase_terminer + j

    return phrase_terminer

def decoder(phrase_deco):

x = int(input("chiffre"))
phrase = 'ceci'
print(coder(phrase))

